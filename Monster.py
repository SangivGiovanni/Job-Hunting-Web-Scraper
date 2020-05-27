import requests
from bs4 import BeautifulSoup


def monster(a, b):

    url_m = "https://www.monster.co.uk/jobs/search?q=" + a + "&where=" + b + "&cy=uk&client=power&stpage=1&page=4"
    page_m = requests.get(url_m)

    soup_m = BeautifulSoup(page_m.content, 'html.parser')
    results_m = soup_m.find(id="SearchResults")

    job_elements_m = results_m.find_all('div', class_='flex-row')
    print("\n")
    print("\n")
    print("RESULTS FROM MONSTER:")
    print("\n")
    print("\n")

    for i in job_elements_m:
        title = i.find('h2', class_='title')
        company = i.find('div', class_='company')
        location = i.find('div', class_='location')
        link = i.find('a')['href']

        if None in (title, company, location):
            continue
        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        print(link)
        print()
