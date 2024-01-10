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

class Category:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.recuperer_categories()

    def __repr__(self):
        return self.title, self.link

    def __str__(self):
        return f"Title: {self.title}\nLink: {self.link}"




