import requests
from bs4 import BeautifulSoup

#r = requests.get('https://www.khudra.com.np/blog')

#soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())

#print(soup.find_all('h5', class_='product-item__title'))
#print(soup.find_all('a').prettify())

'''print(soup.select_one('.product-item__title')) # select only one data
print(soup.select('.product-item__title')) # all the data ain list format

product_lists = soup.select('.title')

for products in product_lists:
    product_title = products.text'''


while True:
    r = requests.get('https://www.khudra.com.np')
    print(r.status_code)
