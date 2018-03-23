import os
import requests
import bs4 as bs
import csv
import re

with open("countries.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        countryCode = (row['Symbol'])
        countryName = (row['Country'])
        response = requests.get('https://www.cia.gov/library/publications/the-world-factbook/geos/' + countryCode +'.html')
        soup = bs.BeautifulSoup(response.text, 'lxml')
        mainBlock = soup.find("div", {"class": "main-block"})
        expandcollapse = mainBlock.find("ul", {"class": "expandcollapse"})
        with open('countryLI.csv', 'a') as csvfile:
            fieldnames = ['Country', 'Code','LICount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
            writer.writeheader()
            i = 0
            for li in expandcollapse:
                i += 1
            writer.writerow({'Country': countryName , 'Code': countryCode,'LICount': i})
