import sqlite3

class Book:
    def __init__(self, title, image_url, alt_text, price, description) :
        self.title = title
        self.image_url = image_url
        self.alt_text = alt_text
        self.price = price
        self.description = description

    def __repr__(self):
        return self.title, self.image_url, self.alt_text, self.price, self.description

    def __str__(self):
        return f"Title: {self.title}\nImage URL: {self.image_url}\nAlt Text: {self.alt_text}\nPrice: {self.price}\nDescription: {self.description}"

    def add_db(controller, book_instance):
        with sqlite3.connect('books.db') as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'")
            table_exists = cursor.fetchone()

            if not table_exists:
                cursor.execute('''
                    CREATE TABLE books (
                        title TEXT,
                        image_url TEXT,
                        alt_text TEXT,
                        price TEXT,
                        description TEXT
                    )
                ''')

                print("---------")
                print("Base de données crée")
                print("---------")

            cursor.execute('''
                INSERT INTO books (title, image_url, alt_text, price, description)
                VALUES (:title, :image_url, :alt_text, :price, :description)
            ''', {
                'title': book_instance.title,
                'image_url': book_instance.image_url,
                'alt_text': book_instance.alt_text,
                'price': book_instance.price,
                'description': book_instance.description
            })

            print("---------")
            print(book_instance.title, "ajouté à la DB!")
            print("---------")
