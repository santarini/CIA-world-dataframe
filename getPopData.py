import os
import requests
import bs4 as bs
import csv
import re

with open("countryLI.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        countryCode = (row['Code'])
        countryName = (row['Country'])
        response = requests.get('https://www.cia.gov/library/publications/the-world-factbook/geos/' + countryCode +'.html')
        soup = bs.BeautifulSoup(response.text, 'lxml')
        population = soup.body.find(text='Population:').findNext('div')
        with open('countryPop.csv', 'a') as csvfile:
            fieldnames = ['Country', 'Code','Population']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
            writer.writerow({'Country': countryName , 'Code': countryCode,'Population': population.text})
