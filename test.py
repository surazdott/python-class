import requests
from bs4 import BeautifulSoup

search = input("Enter job title: ")
r = requests.get(f'https://merojob.com/search/?q={search}')

soup = BeautifulSoup(r.content, 'html.parser')

jobs = soup.select('.media-heading')

with open('jobs.text', 'w') as f:
    for job in jobs:
        f.write(job.find('a').text + '   ')
        f.write(job.find('a').get('href'))
        f.write('\n' + '*' * 20 + '\n')
