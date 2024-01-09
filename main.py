import inquirer

from controllers.controller import  scrapped_page, scrapped_page_category
from views.view import get_url, get_category_url


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
        url = get_url()
        book_instance = scrapped_page(url)
        print(book_instance)

    elif selected_mode == 'Category':
        categoryUrl = get_category_url()
        scrapped_page_category(categoryUrl)

    else:
        print("Mode non reconnu")

main()