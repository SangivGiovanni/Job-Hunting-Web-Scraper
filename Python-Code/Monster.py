import requests
from bs4 import BeautifulSoup


def monster(a, b):

    url_m = "https://www.monster.co.uk/jobs/search?q=" + a + "&where=" + b + "&cy=uk&client=power&stpage=1&page=4"
    page_m = requests.get(url_m)

    soup_m = BeautifulSoup(page_m.content, 'html.parser')
    results_m = soup_m.find(id="SearchResults")

    job_elements_m = results_m.find_all('section', class_='card-content')

    for i in job_elements_m:
        title = i.find('h2', class_='title')
        company = i.find('div', class_='company')
        location = i.find('div', class_='location')
        if None in (title, company, location):
            print(i)
            continue
        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        print()
