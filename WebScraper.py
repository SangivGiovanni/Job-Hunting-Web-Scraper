import requests
from bs4 import BeautifulSoup

print("Chose field: ")
a = input()
print("Chose location (UK): ")
b = input()

URL = "https://www.monster.co.uk/jobs/search?q=" + a + "&where=" + b + "&cy=uk&client=power&stpage=1&page=4"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="SearchResults")

jobElements = results.find_all('section', class_='card-content')

for i in jobElements:
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

    myJobs = results.find_all('h2', string=lambda text: c in text.lower())
    print(len(myJobs))

    if len(myJobs) < 1:
        continue
    else:
        for j in myJobs:
            link = j.find('a')['href']
            print(j.text.strip())
            print(f"Apply here: {link}\n")
        break
