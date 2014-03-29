'''
senatescrape.py

Your objective in this assignment is to write a scraper to retrieve the list of actions that
took place in a given day in the Missouri State Senate. Specifically, you'll need to convert
a page like this:

http://www.senate.mo.gov/14info/BTS_Web/Daily.aspx?SessionType=R&ActionDate=3/26/2014

Into a CSV file formatted like this:

bill_number,sponsor,description,most_recent_action

Some bills can list more than one action for a given day, so be mindful to only get the most
recent one (hint: it's safe to assume it's the last action listed).

I've included a small bit of code below to get you started. The assignment is due next Wednesday,
April 9th. If you have any questions, refer to the screencasts and example code we wrote for class.
Everything you'll need to finish the assignment is there.

For extra credit (or students who have already taken my scraping class), you can also opt into a
second part of the assignment. Namely, use this data to build something useful. Be creative, but think
about how this data might be used in an actual newsroom context. You can mix in other data, build
a simple tool, or anything else you can think of.
'''

########## IMPORT YOUR NECESSARY MODULES HERE ##########


########## INPUTS AND OUTPUTS ##########

# Scrape this page to start
url = 'http://www.senate.mo.gov/14info/BTS_Web/Daily.aspx?SessionType=R&ActionDate=3/26/2014'

# Your output should go in this before it's saved to CSV
output_table = []

########## YOUR CODE GOES HERE ##########