import requests
from bs4 import BeautifulSoup
import csv

print('Now starting the web scrapper \n')

edmunds = 'https://www.edmunds.com/'
zebra = 'https://www.thezebra.com/auto_insurance/vehicles/'

car_makes = ['ford', 'honda', 'hyundai', 'toyota']
car_models = ['escape', 'cr-v','santa-fe', 'rav4']
year = '2017'


def makeSoup(link):
    page = requests.get(link, headers = {'User-Agent' : 'Mozilla/5.0'})
    html = page.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def formatLines(make,model,msrp,resale,insurance_list,maintancance_list):
    data_list = []
    data_list.append(make)
    data_list.append(model)
    data_list.append(msrp)
    data_list.append(resale)
    for i in range(len(insurance_list)):
        data_list.append(insurance_list[i])
    for i in range(len(maintancance_list)):
        data_list.append(insurance_list[i])
    
    return data_list

with open('car_data.csv', mode = 'w') as car_data:
    car_writer = csv.writer(car_data, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    car_writer.writerow(['Make','Model','MSRP','Resale Value', 'Insurance1','Insurance2','Insurance3','Insurance4','Insurance5','Maintainance1','Maintainance2','Maintainance3','Maintainance4','Maintainance5'])
    
    for car in range(len(car_makes)):
        
        print('Working on '+ car_makes[car] + ' ' + car_models[car])
        edmunds_weblink = edmunds + car_makes[car] + '/' + car_models[car] + '/' + year
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

        print('Printing to csv \n')
        car_writer.writerow(formatLines(car_makes[car],car_models[car],msrp,resale_price,insurance,maintainance))

print('Scrape complete')