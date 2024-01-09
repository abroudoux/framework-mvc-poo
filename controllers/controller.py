import requests
import sqlite3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from models.models import Book


def scrappedPage(url) :
    pageParsed = BeautifulSoup(requests.get(url).text, 'html.parser')

    active_div = pageParsed.find('div', class_='item active')

    if active_div :
        img_tag = active_div.find('img')

        if img_tag:
            relative_url = img_tag['src']
            absolute_url = urljoin(url, relative_url)
            image_url = absolute_url
            alt_text = img_tag['alt']
        else:
            image_url = "Image non trouvée"
            alt_text = "Alt non trouvé"
    else:
        image_url = "Image non trouvée"
        alt_text = "Alt non trouvé"

    titleParsed = pageParsed.find('h1')
    title = titleParsed.text if titleParsed else "Titre non trouvé"

    priceParsed = pageParsed.find('p', 'price_color')
    price = priceParsed.text if priceParsed else "Prix non trouvé"

    description_div = pageParsed.find('div', id='product_description')
    description_paragraph = description_div.find_next_sibling('p')
    description = description_paragraph.text if description_paragraph else "Description non trouvée"

    book_instance = Book(title, image_url, alt_text, price, description)

    saveDb(book_instance)

    return book_instance



def saveDb(book_instance):

    conn = sqlite3.connect('local_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            title TEXT,
            image_url TEXT,
            alt_text TEXT,
            price TEXT,
            description TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO books (title, image_url, alt_text, price, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (book_instance.title, book_instance.image_url, book_instance.alt_text, book_instance.price, book_instance.description))

    conn.commit()
    conn.close()
