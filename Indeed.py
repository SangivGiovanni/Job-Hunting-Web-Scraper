import requests
from bs4 import BeautifulSoup


def indeed(a, b):

    page_count = [0, 10, 20, 30, 40, 50, 60, 70]
    for j in page_count:
        url_i = "https://www.indeed.co.uk/jobs?q=" + a + "&l=" + b + "&start=" + str(j)
        page_i = requests.get(url_i)

        soup_i = BeautifulSoup(page_i.content, 'html.parser')
        result_i = soup_i.find(id="resultsCol")

        job_elements_i = result_i.find_all('div', class_='jobsearch-SerpJobCard')
        if j == 0:
            print("\n")
            print("\n")
            print("RESULTS FROM INDEED:")
            print("\n")
            print("\n")

        for i in job_elements_i:
            title = i.find('h2', class_='title')
            company = i.find('span', class_='company')
            location = i.find('div', class_='location accessible-contrast-color-location')
            link = "https://www.indeed.co.uk" + i.find('a')['href']

            if None in (title, company, location):
                continue
            print(title.text.strip())
            print(company.text.strip())
            print(location.text.strip())
            print(link)
            print()
