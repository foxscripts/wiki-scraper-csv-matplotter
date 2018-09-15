from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import numpy as np
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
csvWrite.writerow([ 'Regional Rank','International Rank', 'Countries', 'HDI2015', 'HDI2014', 'Change'])

hdi_table = urlContent.find('table', {'class':'wikitable'})
rows = hdi_table.find_all('tr')

for row in rows:
	hdi_2015 = row.find_all('td')
	hdi_2015 = [x.text.strip() for x in hdi_2015]
	print(hdi_2015)
	print()
	csvWrite.writerows([hdi_2015])

csvFile.close()

x = []
y = []

with open('HDI.csv', 'r') as input_file:
	plots = csv.reader(input_file, skipinitialspace=False, delimiter=' ')
	for cols in plots:
		if len(cols) == 6:
			x.append(int(cols[3]))
			y.append(int(cols[4]))



plt.plot(x, y, label='Loaded from file!', color='g')
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.title('Asian_and_Oceania_countries_by_HDI_2015')
plt.legend()
plt.show()