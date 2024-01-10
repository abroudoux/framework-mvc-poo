import inquirer

class View:
    def __init__(self):
        self.get_mode()

    def get_url():
        url = input("De quel livre voulez-vous obtenir les informations ? ")
        return url

    def get_category_url():
        category_list = [
            inquirer.List('category',
                        message="Choisissez votre catégorie",
                        choices=['Travel', 'Mystery'],
                    ),
        ]

        answers = inquirer.prompt(category_list)
        selected_category = answers["category"]

        if selected_category == 'Travel':
            url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
            return url
        elif selected_category == 'Mystery':
            url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
            return url
        else:
            print("Mode non reconnu")

    def get_mode(self):
        questions = [
            inquirer.List('mode',
                        message="Que voulez-vous récupérer ? ",
                        choices=['Book', 'Category'],
                    ),
        ]
        answers = inquirer.prompt(questions)
        selected_mode = answers["mode"]

        if selected_mode == 'Book':
            return self.get_url
        elif selected_mode == 'Category':
            return self.get_category_url
        else:
            print("Mode non reconnu")
