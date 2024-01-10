import inquirer

class View:
    def __init__(self, mode_config, category_config=None):
        self.url = None
        self.category_config = category_config
        self.mode_config = mode_config

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
        else:
            for mode in self.mode_config:
                if mode == selected_choice:
                    return selected_choice
            else:
                print("Mode non reconnu")
                return None

    def get_book_url(self):
        url = input("De quel livre voulez-vous obtenir les informations ? ")
        return url

    def get_category_url(self):
        categories = [category['name'] for category in self.category_config]

        selected_choice = self.__show_questions("Que voulez-vous faire ?", categories)

        for category in self.category_config:
            if category['name'] == selected_choice:
                return category['url']
