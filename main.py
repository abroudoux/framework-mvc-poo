import inquirer

from controllers.controller import scrappedPage
from views.view import getUrl, getCategory


def main () :

    questions = [
        inquirer.List('mode',
                    message="Que voulez-vous récupérer ? ",
                    choices=['Book', 'Category'],
                ),
    ]

    answers = inquirer.prompt(questions)
    selected_mode = answers["mode"]

    if selected_mode == 'Book':
        url = getUrl()
        book_instance = scrappedPage(url)
        print(book_instance)

    elif selected_mode == 'Category':
        categoryUrl = getCategory()
        print(categoryUrl)

    else:
        print("Mode non reconnu")

main()