"""
~ scrape a website ~

We are going to scrape a simple web page.

The steps:

- Inspect the source of the page and note the pattern
- Use `requests` to fetch the page
- Use `BeautifulSoup` to parse the HTML into Python objects
- Target the elements on the page with the data you want

First, we're going to practice on an HTML file saved locally.

"""

from bs4 import BeautifulSoup

with open('../practice-table.html', 'r') as html_file:
    html_code = html_file.read()
    soup = BeautifulSoup(html_code, 'html.parser')
    
    # find table by position on the page
    # find_all returns a list of matching elements, and we want the second ([1]) one
    # song_table = soup.find_all('table')[1]
    
    # by class name
    # => with `find`, you can pass in a dictionary of element attributes to match on
    # song_table = soup.find('table', {'class': 'song-table'})
    
    # by ID
    # song_table = soup.find('table', {'id': 'my-cool-table'})
    
    # by style
    song_table = soup.find('table', {'style': 'width: 95%;'})
    
    # get table rows but skip the header row
    # more on list slicing: http://pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
    table_rows = song_table.find_all('tr')[1:]
    
    for row in table_rows:
        # get a list of cells in the row
        cols = row.find_all('td')
        
        # the track number is is in the first ([0]) "column"
        # the `.string` attribute gets the contents of a BeautifulSoup Tag object
        track_number = cols[0].string
        
        # the song title is in the second ([1]) "column"
        song_title = cols[1].string

        print(track_number + '.', song_title)


"""
Now let's scrape an actual page -- a table of certified lead burn instructors in Texas.
"""

import requests

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
