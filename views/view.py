import inquirer


def getUrl() :
    url = input("De quel livre voulez-vous obtenir les informations ? ")
    return url

def getCategory() :
    categoryList = [
        inquirer.List('category',
                    message="Choisissez votre catégorie : ",
                    choices=['Travel', 'Mystery'],
                ),
    ]

    answers = inquirer.prompt(categoryList)
    selected_category = answers["category"]
    print(selected_category)

    if selected_category == 'Travel':
        url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
        return url

    elif selected_category == 'Mystery':
        url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
        return url

    else :
        print("Mode non reconnu")
