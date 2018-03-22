import os
import requests
import bs4 as bs
import csv
import re
    
response = requests.get('https://www.cia.gov/library/publications/the-world-factbook/geos/af.html')
soup = bs.BeautifulSoup(response.text, 'lxml')
countrySelection = soup.find('select')
for row in countrySelection.findAll('option'):
    countryCode = re.search('<option value="../geos/(.*).html">', str(row))
    print(countryCode)
    print(row.text)
