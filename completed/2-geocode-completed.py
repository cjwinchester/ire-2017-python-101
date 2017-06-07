"""
~ geocoding ~

You can use Python to geocode addresses in a data file. `geopy` is one library that will help you do this. It gives you several options for geocoing; we're going to use Google's geocoder.

The steps:
- create a new geocoder instance
- open the data file
- loop over the rows
- inside the loop, construct an address to feed to the geocoder
- geocode the address and print the lat/lng returned

"""


# import the Google geocoder from geopy
# import Python's csv and time libaries
from geopy.geocoders import GoogleV3
import csv
import time

# Make a geolocator object
# Set the `timeout` keyword argument to 5 (seconds)
geolocator = GoogleV3(timeout=5)

# in a `with` block, open the file to read from and the file to write to
with open('../data/payday.csv', 'r', newline='') as address_file:

    # make a DictReader object
    reader = csv.DictReader(address_file)
    
    # start for loop here
    for row in reader:

        # Put the address in a Google-recognizable string: ADDRESS, CITY, STATE ZIP
        addr = '{} {} {}, {}, {}'.format(
            row['STADDR'].strip(),
            row['STADDR2'].strip(),
            row['CITY'],
            row['STATE'],
            row['ZIP']
        )
        
        # Geocode that string
        location = geolocator.geocode(addr)
        
        # print the address and results
        print(addr, location.latitude, location.longitude)
        
        # Before we do all of this with the next row, pause for two seconds.
        time.sleep(2)

# Alert us with a printed message when this completes and close both files.
print('All done!')