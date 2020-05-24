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


role = True

while role:

    print("Chose job role: ")
    i = input()
    if i == "/exit":
        break

    myJobsi = resulti.find_all('h2', string=lambda text: i in text.lower())
    print(len(myJobsi))

    if len(myJobsi) < 1:
        continue
    else:
        print("Search results from Indeed: ")
        print("\n")
        for j in myJobsi:
            link = j.find('a')['href']
            print(j.text.strip())
            print(f"Apply here: {link}\n")
        break
