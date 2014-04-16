import urllib2, csv
from BeautifulSoup import BeautifulSoup

url = 'http://www.senate.mo.gov/14info/BTS_Web/Daily.aspx?SessionType=R&ActionDate=4/08/2014'
html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html)
results_table = soup.find('div', attrs={'align' : 'left'})

output_table = []

for dl in results_table.findAll('dl'):
    output_row = []

    bill_number = dl.findAll('a')[0].text
    sponsor = dl.findAll('a')[1].text
    text = dl.find('dt').text.replace("&nbsp;", ' ')
    most_recent_action = dl.findAll('dd')[-1].text

    output_row.append(bill_number)
    output_row.append(sponsor)
    output_row.append(text)
    output_row.append(most_recent_action)

    output_table.append(output_row)

print output_table


# outfile = open('out.csv', 'w')
# writer = csv.writer(outfile)
# writer.writerows(output_table)