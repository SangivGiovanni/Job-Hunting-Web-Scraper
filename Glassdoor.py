import requests
from bs4 import BeautifulSoup


def indeed(a, b):

    page_count = [1, 2, 3, 4, 5, 6, 7]
    for j in page_count:
        url_g = "https://www.glassdoor.co.uk/Job/" + b + "-" + a + "-SRCH_IL.0,6_IC2671300_KO7,17_IP" + str(j) + ".htm"
        page_g = requests.get(url_g)

        soup_g = BeautifulSoup(page_g.content, 'html.parser')
        result_g = soup_g.find(class_="jlGrid")

        job_elements_g = result_g.find_all('li', class_='jl react-job-listing gdGrid')
        if j == 0:
            print("\n")
            print("\n")
            print("RESULTS FROM GLASSDOOR:")
            print("\n")
            print("\n")

        for i in job_elements_g:
            title = i.find('a', class_='jobInfoItem jobTitle jobLink')
            company = i.find('div', class_='jobInfoItem jobEmpolyerName')
            location = i.find('span', class_='subtle loc css-nq3w9f pr-xxsm')
            link = i.find('a')['href']

            if None in (title, company, location):
                continue
            print(title.text.strip())
            print(company.text.strip())
            print(location.text.strip())
            print(link)
            print()


indeed("programmer", "london")
