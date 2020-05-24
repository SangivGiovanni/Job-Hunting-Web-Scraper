import requests
from bs4 import BeautifulSoup


def indeed(a, b):

    url_i = "https://www.indeed.co.uk/jobs?q=" + a + "&l=" + b
    page_i = requests.get(url_i)

    soup_i = BeautifulSoup(page_i.content, 'html.parser')
    result_i = soup_i.find(id="resultsCol")

    job_elements_i = result_i.find_all('div', class_='jobsearch-SerpJobCard')

    for i in job_elements_i:
        title = i.find('h2', class_='title')
        company = i.find('span', class_='company')
        location = i.find('div', class_='location accessible-contrast-color-location')
        if None in (title, company, location):
            print(i)
            print()
            continue
        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        print()
