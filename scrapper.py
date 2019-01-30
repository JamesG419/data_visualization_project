import requests
from bs4 import BeautifulSoup
import csv

print('Now starting the web scrapper')

edmunds = 'https://www.edmunds.com/'
zebra = 'https://www.thezebra.com/auto_insurance/vehicles/'

car_makes = ['ford', 'honda', 'hyundai', 'toyota']
car_models = ['escape', 'cr-v','santa-fe', 'rav-4']
year = '2017'


def makeSoup(link):
    page = requests.get(link, headers = {'User-Agent' : 'Mozilla/5.0'})
    html = page.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

for i in car_makes:
    
    edmunds_weblink = edmunds + car_makes[i] + '/' + car_models[i] + '/' + year
    price_soup = makeSoup(edmunds_weblink)

    #pulls price data
    price_soup = price_soup.find_all('div', class_ = 'size-30 font-weight-bold text-info text-left')
    price_string = price_soup[0].text
    price_string_split = price_string.split(' - ')
    resale_price = price_string_split[0]
    msrp = price_string_split[1]

    #collect insurance and maintanence data
    i_m_link = edmunds_weblink + '/cost-to-own'
    i_m_soup = makeSoup(i_m_link)

    i_m_strings = i_m_soup.find_all('li', class_ = 'first')
    insurance_tree = i_m_strings[6]
    insurance_tags = insurance_tree.find_all_next('li', limit = 5)

    insurance = []
    for i in range(len(insurance_tags)):
        insurance.append(insurance_tags[i].text)

    maintianence_tree = i_m_strings[7]
    maintainance_tags = insurance_tree.find_all_next('li', limit = 5)

    maintainance = []
    for i in range(len(maintainance_tags)):
        maintainance.append(maintainance_tags[i].text)

