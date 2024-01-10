import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from models.model import Book
from views.view import View
from sql.db import save_to_db

class Controller:
    def __init__():
        View()

    def scrapped_page(url):
        page_parsed = BeautifulSoup(requests.get(url).text, 'html.parser')

        active_div = page_parsed.find('div', class_='item active')

        if active_div:
            img_tag = active_div.find('img')

            if img_tag:
                relative_url = img_tag['src']
                image_url= urljoin(url, relative_url)
                alt_text = img_tag['alt']
            else:
                image_url = "Image non trouvée"
                alt_text = "Alt non trouvé"
        else:
            image_url = "Image non trouvée"
            alt_text = "Alt non trouvé"

        title_parsed = page_parsed.find('h1')
        title = title_parsed.text if title_parsed else "Titre non trouvé"

        price_parsed = page_parsed.find('p', 'price_color')
        price = price_parsed.text if price_parsed else "Prix non trouvé"

        description_div = page_parsed.find('div', id='product_description')
        description_paragraph = description_div.find_next_sibling('p')
        description = description_paragraph.text if description_paragraph else "Description non trouvée"

        book_instance = Book(title, image_url, alt_text, price, description)

        save_to_db(book_instance)

        return book_instance

    def scrapped_page_category(self, categoryUrl):
        all_books_links = []

        while True:
            page_category_parsed = BeautifulSoup(requests.get(categoryUrl).text, 'html.parser')

            links_books = []
            articles = page_category_parsed.find_all('article', 'product_pod')

            for article in articles:
                a_tag = article.find('a')

                if a_tag:
                    book_link = urljoin(categoryUrl, a_tag['href'])
                    links_books.append(book_link)

            all_books_links.extend(links_books)

            for link_book in links_books:
                print(link_book)
                self.scrapped_page(link_book)
                print("------------")

            pager_ul = page_category_parsed.find('ul', class_='pager')
            if pager_ul:
                next_li = pager_ul.find('li', class_='next')
                if next_li:
                    next_a_tag = next_li.find('a')
                    if next_a_tag:
                        categoryUrl = urljoin(categoryUrl, next_a_tag['href'])
                    else:
                        break
                else:
                    break
            else:
                break

        return all_books_links

    def recuperer_categories(url):
        page_parsed = BeautifulSoup(requests.get(url).text, 'html.parser')

        category_links = []
        category_div = page_parsed.find('ul', class_='nav nav-list')

        for links in category_div:
            a_tag = links.find('a')

            if a_tag:
                category_link = urljoin(url, a_tag['href'])
                category_links.append(category_link)



