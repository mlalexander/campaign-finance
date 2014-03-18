import urllib2
from BeautifulSoup import BeautifulSoup

html = urllib2.urlopen('https://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp')

soup = BeautifulSoup(html)
results_table = soup.find('table', attrs={'class': 'resultsTable'})

output_table = []

for tr in results_table.findAll('tr'):
    
    output_row = []
    tds = tr.findAll('td')
    
    for td in tds:
        scraped_value = td.text.replace('&nbsp;', '')
        output_row.append(scraped_value)

    output_table.append(output_row)

print output_table