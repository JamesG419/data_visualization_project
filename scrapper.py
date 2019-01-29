import requests
from bs4 import BeautifulSoup
import csv

print('Now starting the web scrapper')

edmunds = 'https://www.edmunds.com/'
zebra = 'https://www.thezebra.com/auto_insurance/vehicles/'

car_makes = ['ford', 'honda', 'hyundai', 'toyota']
car_models = ['escape', 'cr-v','santa-fe', 'rav-4']
year = '2017'


