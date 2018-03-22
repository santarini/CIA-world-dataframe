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
mainBlock = soup.find("div", {"class": "main-block"})
expandcollapse = mainBlock.find("ul", {"class": "expandcollapse"})
#introductionSection = expandcollapse.findAll('li')[1]
geographySection = expandcollapse.findAll('li')[3]
peopleAndSocietySection = expandcollapse.findAll('li')[5]
#population
population = peopleAndSocietySection.findAll("div", {"class": "category_data"})[0]
populationGrowthRate = peopleAndSocietySection.findAll("div", {"class": "category_data"})[4]
birthRate = peopleAndSocietySection.findAll("div", {"class": "category_data"})[5]
deathRate = peopleAndSocietySection.findAll("div", {"class": "category_data"})[6]
print(deathRate)
