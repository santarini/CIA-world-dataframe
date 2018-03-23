import os
import requests
import bs4 as bs
import csv
import re

with open("cleanCountries.csv") as csvfileA:
    reader = csv.DictReader(csvfileA)
    with open('countryPop.csv', 'a') as csvfileB:
        fieldnames = ['Country', 'Code','Population']
        writer = csv.DictWriter(csvfileB, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
        for row in reader:
            countryName = (row['Country'])
            countryCode = (row['Code'])
            response = requests.get('https://www.cia.gov/library/publications/the-world-factbook/geos/' + countryCode +'.html')
            soup = bs.BeautifulSoup(response.text, 'lxml')
            
            #population
            population = soup.body.find(text='Population:').findNext('div')
            population = population.text
            if "(" in population:
                dateEst = population.split('(')[1]
                population = population.split('(')[0]
            if "total:" in population:
                population = population.split('total:')[1]
            if "United Kingdom" in population:
                population = population.split('United Kingdom')[1]
            
            #write the data to csv
            writer.writerow({'Country': countryName , 'Code': countryCode,'Population': population})
