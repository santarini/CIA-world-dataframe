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
totalMedianAge = peopleAndSocietySection.findAll("span", {"class": "category_data"})[15]
maleMedianAge = peopleAndSocietySection.findAll("span", {"class": "category_data"})[16]
femaleMedianAge = peopleAndSocietySection.findAll("span", {"class": "category_data"})[17]
populationGrowthRate = peopleAndSocietySection.findAll("div", {"class": "category_data"})[4]
birthRate = peopleAndSocietySection.findAll("div", {"class": "category_data"})[5]
deathRate = peopleAndSocietySection.findAll("div", {"class": "category_data"})[6]
netMigration = peopleAndSocietySection.findAll("div", {"class": "category_data"})[7]
totalSexRatio = peopleAndSocietySection.findAll("span", {"class": "category_data"})[31]
motherMeanAgeAtBirth = peopleAndSocietySection.findAll("div", {"class": "category_data"})[10]
maternalMortalityRate = peopleAndSocietySection.findAll("div", {"class": "category_data"})[11]
totalInfantMortalityRate = peopleAndSocietySection.findAll("span", {"class": "category_data"})[34]
totalLifeExpectancy =peopleAndSocietySection.findAll("span", {"class": "category_data"})[38]
longName = peopleAndSocietySection.findAll("span", {"class": "category_data"})[61]
shortName = peopleAndSocietySection.findAll("span", {"class": "category_data"})[62]
govType = peopleAndSocietySection.findAll("div", {"class": "category_data"})[35]
capital = peopleAndSocietySection.findAll("span", {"class": "category_data"})[67]
timeCode = peopleAndSocietySection.findAll("span", {"class": "category_data"})[69]
indDay = peopleAndSocietySection.findAll("div", {"class": "category_data"})[37]
natHoliday = peopleAndSocietySection.findAll("div", {"class": "category_data"})[38]
GDP = peopleAndSocietySection.findAll("div", {"class": "category_data"})[52]
GDPRealGrowth = peopleAndSocietySection.findAll("div", {"class": "category_data"})[56]
GDPPerCapita = peopleAndSocietySection.findAll("div", {"class": "category_data"})[59]

print(GDPPerCapita)


