import os
import requests
import bs4 as bs
import csv
import re

with open("cleanCountries.csv") as csvfileA:
    reader = csv.DictReader(csvfileA)
    with open('countryData.csv', 'a') as csvfileB:
        fieldnames = ['Region','Code', 'Short Name','Long Name','Population', 'Population Growth Rate', 'GDP (PPP)', 'GDP per Capita', 'GDP Growth Rate']
        writer = csv.DictWriter(csvfileB, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
        for row in reader:
            regionName = (row['Country'])
            countryCode = (row['Code'])
            response = requests.get('https://www.cia.gov/library/publications/the-world-factbook/geos/' + countryCode +'.html')
            soup = bs.BeautifulSoup(response.text, 'lxml')

            #Country name long and short:
            if "Country name:" not in soup.text:
                shortName = 'Not listed'
                longName = 'Not listed'
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
                population = (float(population) * 10**6)

            #population growth rate
            if "Population growth rate:" not in soup.text:
                populationGrowth = 'Not listed'
            else:
                populationGrowth = soup.body.find(text='Population growth rate:').findNext('div')
                populationGrowth = populationGrowth.text
            if "(" in populationGrowth:
                popGrowthDateEst = populationGrowth.split('(')[1]
                populationGrowth = populationGrowth.split('(')[0]
            
            #GDP (purchasing power parity):
            if "GDP (purchasing power parity):" not in soup.text:
                GDPppp = 'Not listed'
            else:
                GDPppp = soup.body.find(text='GDP (purchasing power parity):').findNext('div')
                GDPppp = GDPppp.text
            if "(" in GDPppp:
                GDPpppDateEst = GDPppp.split('(')[1]
                GDPppp = GDPppp.split('(')[0]
            if "million" in GDPppp:
                GDPppp = GDPppp.split('million')[0]
                GDPppp = GDPppp[1:]
                GDPppp = float(GDPppp) * 10**6
            elif "billion" in GDPppp:
                GDPppp = GDPppp.split('billion')[0]
                GDPppp = GDPppp[1:]
                GDPppp = float(GDPppp) * 10**9
            elif "trillion" in GDPppp:
                GDPppp = GDPppp.split('trillion')[0]
                GDPppp = GDPppp[1:]
                GDPppp = float(GDPppp)
                GDPppp = int(GDPppp) * 10**12
                
            #GDP - per capita (PPP):
            if "GDP - per capita (PPP):" not in soup.text:
                GDPcapita = 'Not listed'
            else:
                GDPcapita = soup.body.find(text='GDP - per capita (PPP):').findNext('div')
                GDPcapita = GDPcapita.text
            if "(" in GDPcapita:
                GDPcapitaDateEst = GDPcapita.split('(')[1]
                GDPcapita = GDPcapita.split('(')[0]


            #GDP - real growth rate:
            if "GDP - real growth rate:" not in soup.text:
                GDPgrowth = 'Not listed'
            else:
                GDPgrowth = soup.body.find(text='GDP - real growth rate:').findNext('div')
                GDPgrowth = GDPgrowth.text
            if "(" in GDPgrowth:
                GDPgrowthDateEst = GDPgrowth.split('(')[1]
                GDPgrowth = GDPgrowth.split('(')[0]
            
            
            #Median age:
            if "Median age:" not in soup.text:
                medianAge = 'Not listed'
            else:
                medianAge = soup.body.find(text='Median age:').findNext('div')
                medianAge = medianAge.text
            if "(" in GDPgrowth:
                medianAgeDateEst = medianAge.split('(')[1]
                medianAge = medianAge.split('(')[0]
            if "total: " in medianAge:
                medianAge = medianAge.split('total: ')[1]
            if "years" in medianAge:
                medianAge = medianAge.split('years')[0]
            
            #print to csv
            writer.writerow({'Region': regionName,'Code': countryCode, 'Short Name': shortName,'Long Name': longName,'Population': population, 'Population Growth Rate': populationGrowth, 'GDP (PPP)':GDPppp , 'GDP per Capita':GDPcapita, 'GDP Growth Rate':GDPgrowth})
            
