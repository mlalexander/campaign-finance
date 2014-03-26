import urllib2
from BeautifulSoup import BeautifulSoup

html = urllib2.urlopen('https://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp')

soup = BeautifulSoup(html)
results_table = soup.find('table', attrs={'class': 'resultsTable'})

output_list = [] # This corresponds to the table

for tr in results_table.findAll('tr'):

    row_list = []

    for td in tr.findAll('td'):
        row_list.append(td.text.replace('&nbsp;', ''))

    output_list.append(row_list)

print output_list