import requests
from bs4 import BeautifulSoup
import csv

print('Now starting the web scrapper')

edmunds = 'https://www.edmunds.com/'
zebra = 'https://www.thezebra.com/auto_insurance/vehicles/'

car_makes = ['ford', 'honda', 'hyundai', 'toyota']
car_models = ['escape', 'cr-v','santa-fe', 'rav-4']
year = '2017'


for i in car_makes:
    weblink = edmunds + car_makes[i] + '/' + car_models[i] + '/' + year

    page = requests.get(weblink, headers = {'User-Agent' : 'Mozilla/5.0'})
    html = page.text 
    soup = BeautifulSoup(html, 'html.parser')

    #pulls price data
    price_soup = soup.find_all('div', class_ = 'size-30 font-weight-bold text-info text-left')
    price_string = price_soup[0].text
    price_string_split = price_string.split(' - ')
    resale_price = price_string_split[0]
    msrp = price_string_split[1]

    