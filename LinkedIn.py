import requests 
from bs4 import BeautifulSoup

pages = range(1,6)

def linkedin(a,b)
    for page in pages:

        URL = 'https://uk.linkedin.com/jobs/search?keywords='+ a +'%20&location='+ b +'&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum='+ str(page)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find('section', class_ = 'results__list')

        job_cards = results.find_all('li', class_ = 'job-result-card')

        for job_card in job_cards:

            title = job_card.find('h3', class_='result-card__title')
            company = job_card.find('a', class_='result-card__subtitle-link')
            location = job_card.find('span', class_="job-result-card__location")

            link = job_card.find('a', class_="result-card__full-card-link")['href']

            print(title.text)
            print(company.text)
            print(location.text)
            print(link)
            print()