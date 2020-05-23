import requests
from bs4 import BeautifulSoup

print("Chose field: ")
a = input()
print("Chose location (UK): ")
b = input()

URLm = "https://www.monster.co.uk/jobs/search?q=" + a + "&where=" + b + "&cy=uk&client=power&stpage=1&page=4"
URLi = "https://www.indeed.co.uk/jobs?q=" + a + "&l=" + b
pagem = requests.get(URLm)
pagei = requests.get(URLi)

soupm = BeautifulSoup(pagem.content, 'html.parser')
resultsm = soupm.find(id="SearchResults")
soupi = BeautifulSoup(page1.content, 'html.parser')
resulti = soupi.find(id="resultsCol")

jobElementsm = resultsm.find_all('section', class_='card-content')
jobElementsi = resultsi.find_all('div', class_='jobsearch-SerpJobCard')

for i in jobElementsm:
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

role = True

while role:

    print("Chose job role: ")
    c = input()
    if c == "/exit":
        break

    myJobsm = resultsm.find_all('h2', string=lambda text: c in text.lower())
    print(len(myJobsm))
    print("\n")

    if len(myJobsm) < 1:
        continue
    else:
        print("Serch results from Monster: ")
        print("\n")
        for j in myJobsm:
            link = j.find('a')['href']
            print(j.text.strip())
            print(f"Apply here: {link}\n")
        break
