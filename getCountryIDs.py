import os
import requests
import bs4 as bs
import csv
import re


#create source folder if it doesnt exist yet
if not os.path.exists('country_dfs'):
    os.makedirs('country_dfs')
    
response = requests.get('https://www.cia.gov/library/publications/the-world-factbook/geos/af.html')
soup = bs.BeautifulSoup(response.text, 'lxml')
countrySelection = soup.find('select')
with open('country_dfs/countries.csv', 'a') as csvfile:
    fieldnames = ['Symbol', 'Country']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
    writer.writeheader()
    for row in countrySelection.findAll('option'):
        valueStr = row.get('value')
        start = "../geos/"
        end = ".html"
        countryCode = valueStr[len(start):-len(end)]
        writer.writerow({'Symbol': countryCode,'Country': row.text})
