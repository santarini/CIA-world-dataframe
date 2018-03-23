import os
import requests
import bs4 as bs
import csv
import re


with open("cleanCountries.csv") as csvfileA:
    reader = csv.DictReader(csvfileA)
    for row in reader:
        countryName = (row['Country'])
        countryCode = (row['Code'])
        response = requests.get('https://www.cia.gov/library/publications/the-world-factbook/geos/' + countryCode + '.html')
        soup = bs.BeautifulSoup(response.text, 'lxml')
                
        #population growth rate
        if "Population growth rate:" not in soup.text:
            populationGrowth = 'None'
        else:
            populationGrowth = soup.body.find(text='Population growth rate:').findNext('div')
            populationGrowth = populationGrowth.text
        if "(" in populationGrowth:
            popGrowthDateEst = populationGrowth.split('(')[1]
            populationGrowth = populationGrowth.split('(')[0]


        print(countryName + " " + populationGrowth)
