import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from models.model import Book
from views.view import View

class Controller:
    mode_config = ['Book', 'Category', 'Delete Database', 'Exit']

    def __init__(self):
        category_config = [
            {'name': 'Travel', 'url': 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'},
            {'name': 'Mystery', 'url': 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'},
        ]
        self.view = View(self.mode_config, category_config)
        self.handle_mode()

    def handle_book_url(self):
        self.url = self.view.get_book_url()
        self.scrapped_page_book(self.url)

    def handle_mode(self):
        self.selected_choice = self.view.get_mode()

        if self.selected_choice == 'Exit':
            exit()
        else:
            if self.selected_choice == self.mode_config[0]:
                self.handle_book_url()
            elif self.selected_choice == self.mode_config[1]:
                self.handle_category()
            elif self.selected_choice == self.mode_config[2]:
                self.delete_db()
            else:
                print("Mode non reconnu")

    def handle_category(self):
        self.category_url = self.view.get_category_url()
        self.scrapped_page_category(self.category_url)

    def scrapped_page_book(self, url):
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

        title_parsed = page_parsed.find('h1')
        title = title_parsed.text if title_parsed else "Titre non trouvé"
        price_parsed = page_parsed.find('p', 'price_color')
        price = price_parsed.text if price_parsed else "Prix non trouvé"
        description_div = page_parsed.find('div', id='product_description')
        description_paragraph = description_div.find_next_sibling('p')
        description = description_paragraph.text if description_paragraph else "Description non trouvée"

        book_instance = Book(title, image_url, alt_text, price, description)

        Book.add_db(self, book_instance)

        return book_instance


    def scrapped_page_category(self, category_url):
        all_books_links = []

        while True:
            books_links = []
            page_category_parsed = BeautifulSoup(requests.get(self.category_url).text, 'html.parser')
            articles = page_category_parsed.find_all('article', 'product_pod')

            for article in articles:
                a_tag = article.find('a')

                if a_tag:
                    book_link = urljoin(category_url, a_tag['href'])
                    books_links.append(book_link)

            all_books_links.extend(books_links)

            for link_book in books_links:
                self.scrapped_page_book(link_book)

            pager_ul = page_category_parsed.find('ul', class_='pager')

            if pager_ul:
                next_li = pager_ul.find('li', class_='next')
                if next_li:
                    next_a_tag = next_li.find('a')
                    if next_a_tag:
                        categoryUrl = urljoin(category_url, next_a_tag['href'])
                    else:
                        break
                else:
                    break
            else:
                break

        return all_books_links

    def delete_db(self):
        db_file = 'local_database.db'

        if os.path.exists(db_file):
            os.remove(db_file)
            print("---------")
            print("Base de données supprimée")
            print("---------")
        else:
            print("---------")
            print("La base de données n'existe pas")
            print("---------")
