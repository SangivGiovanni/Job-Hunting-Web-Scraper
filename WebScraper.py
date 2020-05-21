import requests
from bs4 import BeautifulSoup

print("Chose field: ")
a = input()
print("Chose location (UK): ")
b = input()

URL1 = "https://www.monster.co.uk/jobs/search?q=" + a + "&where=" + b + "&cy=uk&client=power&stpage=1&page=4"
URL2 = "https://www.indeed.co.uk/jobs?q=" + a + "&l=" + b
page1 = requests.get(URL1)
page2 = requests.get(URL2)

soup1 = BeautifulSoup(page1.content, 'html.parser')
results1 = soup1.find(id="SearchResults")

jobElements = results1.find_all('section', class_='card-content')

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

    myJobs = results1.find_all('h2', string=lambda text: c in text.lower())
    print(len(myJobs))

    if len(myJobs) < 1:
        continue
    else:
        for j in myJobs:
            link = j.find('a')['href']
            print(j.text.strip())
            print(f"Apply here: {link}\n")
        break
