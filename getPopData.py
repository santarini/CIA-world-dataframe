import os
import requests
import bs4 as bs
import csv
import re

with open("cleanCountries.csv") as csvfileA:
    reader = csv.DictReader(csvfileA)
    with open('countryPop.csv', 'a') as csvfileB:
        fieldnames = ['Country', 'Code','Population', 'Population Growth Rate']
        writer = csv.DictWriter(csvfileB, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
        for row in reader:
            countryName = (row['Country'])
            countryCode = (row['Code'])
            response = requests.get('https://www.cia.gov/library/publications/the-world-factbook/geos/' + countryCode +'.html')
            soup = bs.BeautifulSoup(response.text, 'lxml')

            #Country name long and short:
            if "Country name:" not in soup.text:
                shortName = 'None'
                longName = 'None'
            else:
                longName = soup.body.find(text='Country name:').findNext('div')
                longName = longName.text
                shortName = soup.body.find(text='Country name:').findNext('div').findNext('div')
                shortName = shortName.text
            if "conventional long form: " in longName:
                longName = longName.split('conventional long form: ')[1]
            if "conventional short form: " in shortName:
                shortName = shortName.split('conventional short form: ')[1]
                
            #population data
            population = soup.body.find(text='Population:').findNext('div')
            population = population.text
            if "(" in population:
                popDateEst = population.split('(')[1]
                population = population.split('(')[0]
            if "total:" in population:
                population = population.split('total:')[1]
            if "United Kingdom" in population:
                population = population.split('United Kingdom')[1]
            if "million" in population:
                population = population.split(' million')[0]
                population = (float(population) * 1000000)

            #population growth rate
            if "Population growth rate:" not in soup.text:
                populationGrowth = 'None'
            else:
                populationGrowth = soup.body.find(text='Population growth rate:').findNext('div')
                populationGrowth = populationGrowth.text
            if "(" in populationGrowth:
                popGrowthDateEst = populationGrowth.split('(')[1]
                populationGrowth = populationGrowth.split('(')[0]
            
            #print to csv
            writer.writerow({'Country': countryName , 'Code': countryCode,'Population': population, 'Population Growth Rate': populationGrowth})

