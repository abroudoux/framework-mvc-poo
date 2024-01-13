import inquirer

class View:
    def __init__(self, mode_config):
        self.url = None
        self.mode_config = mode_config
        self.category_config = [
            {'name': 'Travel', 'url': 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'},
            {'name': 'Mystery', 'url': 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'},
        ]

    def __show_questions(self, question, data):
        questions = [
            inquirer.List('mode',
                        message=question,
                        choices=data,
                    ),
        ]
        answers = inquirer.prompt(questions)
        selected_choice = answers["mode"]
        return selected_choice

    def get_mode(self):
        selected_choice = self.__show_questions("Que voulez-vous faire ?", self.mode_config)

        if selected_choice == 'Exit':
            exit()

        if selected_choice in self.mode_config:
            return selected_choice
        else:
            print("Mode non reconnu")
            return None

    def get_book_url(self):
        url = input("De quel livre voulez-vous obtenir les informations ? ")
        return url

    def get_category_url(self):
        categories = [category['name'] for category in self.category_config]

        selected_choice = self.__show_questions("Quelle catégorie voulez-vous sélectionner ?", categories)

        for category in self.category_config:
            if category['name'] == selected_choice:
                return category['url']

    def show_message(self, message_print):
        print(message_print)