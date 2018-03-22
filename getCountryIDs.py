import os
import requests
import bs4 as bs
import csv
import re
    
response = requests.get('https://www.cia.gov/library/publications/the-world-factbook/geos/af.html')
soup = bs.BeautifulSoup(response.text, 'lxml')
countrySelection = soup.find('select')
#print(countrySelection)
for row in countrySelection.findAll('option'):
    valueStr = row.get('value')
    start = "../geos/"
    end = ".html"
    countryCode = valueStr[len(start):-len(end)]
    print(countryCode)
    print(row.text)
