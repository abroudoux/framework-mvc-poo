import requests
from bs4 import BeautifulSoup

url = 'https://annuaire-entreprises.data.gouv.fr/entreprise/mma-828717850'
pageParsed = BeautifulSoup(requests.get(url).text, 'html.parser')

# print(pagePrettier.prettify())

print(pageParsed.prettify())
