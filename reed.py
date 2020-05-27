import requests
from bs4 import BeautifulSoup


pages = range(1,6)

def reed(a,b):
    for page in pages:

        URL = 'https://www.reed.co.uk/jobs/' + a + '-jobs-in-'+ b + '?pageno=' + str(page)
        page = requests.get(URL)


        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find('section', id= 'server-results')

        job_containers = results.find_all('article', class_='job-result')



    for job_elem in job_containers:

        title = job_elem.find('h3', class_='title')
        company =  job_elem.find('a', class_='gtmJobListingPostedBy')
        location = job_elem.find('li', class_='location')
        remove_loc = location.span 
        remove_loc.decompose()
        link = job_elem.find('h3', class_ = 'title')
        job_link = 'https://www.reed.co.uk' + link.find('a')['href']

        print(title.text.strip())
        print(company.text)
        print(location.text.strip())
        print(job_link)
        print()







