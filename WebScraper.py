import requests
# import pprint
from bs4 import BeautifulSoup

URL = "https://www.monster.co.uk/jobs/search/?q=Graduate-" \
      "Programmer&where=London&cy=uk&client=power&stpage=1&page=4&jobid=217308916"
page = requests.get(URL)
# pprint.pprint(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="SearchResults")
# print(results.prettify())

jobElements = results.find_all('section', class_='card-content')

for i in jobElements:
    title = i.find('header', class_='card-header')
    company = i.find('div', class_='company')
    location = i.find('div', class_='location')
    if None in (title, company, location):
        print(i)
        continue
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()
