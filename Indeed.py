import requests
from bs4 import BeautifulSoup

print("Chose field: ")
a = input()
print("Chose location (UK): ")
b = input()

URLi = "https://www.indeed.co.uk/jobs?q=" + a + "&l=" + b
pagei = requests.get(URLi)

soupi = BeautifulSoup(pagei.content, 'html.parser')
resulti = soupi.find(id="resultsCol")

jobElementsi = resulti.find_all('div', class_='jobsearch-SerpJobCard')
print(len(jobElementsi))

for i in jobElementsi:
    title = i.find('h2', class_='title')
    company = i.find('span', class_='company')
    location = i.find('div', class_='location accessible-contrast-color-location')
    if None in (title, company, location):
        print(i)
        continue
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()

