from bs4 import BeautifulSoup
# from matplotlib import pyplot as plt
import requests
import csv

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

url = requests.get('https://en.wikipedia.org/wiki/List_of_countries_in_Asia_and_Oceania_by_Human_Development_Index', headers=headers)
urlContent = BeautifulSoup(url.content, "lxml")

csvFile = open('HDI.csv', 'w')
csvWrite = csv.writer(csvFile)
csvWrite.writerow(['List_of_Asian_and_Oceania_countries_by_Human_Development_Index_2015'])

hdi_table = urlContent.find('table', {'class':'wikitable'})
nation_names = hdi_table.find_all('a')
rows = hdi_table.find_all('tr')

# for nations in nation_names:
# 	nations = nations.get('title')
# 	print(nations)
# 	print()
# 	csvWrite.writerow([nations])

for row in rows:
	hdi_2015 = row.find_all('td')
	hdi_2015 = [x.text.strip() for x in hdi_2015]
	print(hdi_2015)
	print()
	csvWrite.writerow([hdi_2015])

csvFile.close()
