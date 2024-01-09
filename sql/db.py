import sqlite3

def save_to_db(book_instance):
    with sqlite3.connect('local_database.db') as conn:
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
            VALUES (:title, :image_url, :alt_text, :price, :description)
        ''', {
            'title': book_instance.title,
            'image_url': book_instance.image_url,
            'alt_text': book_instance.alt_text,
            'price': book_instance.price,
            'description': book_instance.description
        })

        print("livre ajouté à la DB!")
