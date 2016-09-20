"""
This will grab the data from CricInfo Site about TestMatch Played by Pakistan against England from 1954-till now
"""
#http://stats.espncricinfo.com/ci/engine/stats/analysis.html?search=Pakistan;template=analysis
import requests
from bs4 import BeautifulSoup
url = 'http://stats.espncricinfo.com/ci/engine/team/7.html?class=1;opposition=1;template=results;type=team;view=results'

r = requests.get(url)
html = r.text

#create soup object
soup = BeautifulSoup(html,'lxml')
recs = soup.select('tbody > .data1')

file = open('data_england_test.csv', "w")
for i in range(2,len(recs)):
        single = recs[i].findAll('td')
        file.write(single[0].text + ','+single[1].text+ ','+single[2].text+ ','+single[3].text+ ','+ single[4].text+ ','+single[6].text+ ','+ single[7].text+'\n')

file.close()
