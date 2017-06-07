"""
~ scrape a website ~

We are going to scrape a simple web page.

The steps:

- Inspect the source of the page and note the pattern
- Use `requests` to fetch the page
- Use `BeautifulSoup` to parse the HTML into Python objects
- Target the elements on the page with the data you want

"""

import requests
from bs4 import BeautifulSoup

# define URL
url = 'http://texasagriculture.gov/Portals/0/Reports/PIR/certified_lead_burn_instructors.html'

# fetch it
r = requests.get(url)

# soup the text
soup = BeautifulSoup(r.text, 'html.parser')

# find the table
table = soup.find('table', {'summary': 'CERTIFIED LEAD BURN INSTRUCTORS LIST'})

# find the rows, using slice to leave off
# the header row
rows = table.find_all('tr')[1:]

# loop over the rows
for row in rows:
    cols = row.find_all('td')

    name = cols[1].string.strip()
    addr = cols[2].string.strip()
    city = cols[3].string.strip()
    state = cols[4].string.strip()
    zip_code = cols[5].string.strip()
    phone = cols[6].string.strip()
    eff_date = cols[7].string.strip()

    print([name, addr, city, state, zip_code, phone, eff_date])

"""
EXERCISE:
- Filter the results so that you only print out the instructors from Austin
- Instead of printing, write the results to a CSV
"""
