"""
~ working with data in text files ~

A common thing to do with Python is to process data files. You can use the built-in `csv` module to work with delimited text.

We'll open the files like this:
- inside a `with` block -- notice the indentation on subsequent lines
- in `r` ("read") mode
- as some_variable that gives you a handle to the file object
- with the newline argument set to a blank string

Inside the with block, we'll create a `csv.reader` object and hand it the file object variable as an argument.

You can then _iterate_ over the rows in the data file, with each row as a list of items in the row.
"""

import csv

with open('../data/lotto.csv', 'r', newline='') as infile:
    reader = csv.reader(infile)

    for row in reader:
        county = row[0]
        retailer = row[1]
        address = row[2]
        city = row[3]
        date_claimed = row[4]
        game = row[5]
        amount = row[6]
        claimant_name = row[7]
        claimant_city = row[8]
        claimant_state = row[9]

        # print(city)



"""
You can also use a `csv.DictReader` object instead of a `csv.reader` object, which will treat each row as a dictionary instead of a list. The keys will be the items in the header row.

I like using `csv.DictReader` better because it's easier to keep track of where everything is.
"""

with open('../data/lotto.csv', 'r', newline='') as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        county = row['County']
        retailer = row['Selling Retailer']
        address = row['Business Address']
        city = row['City']
        date_claimed = row['Date Claimed']
        game = row['Game']
        amount = row['Prize Amount']
        claimant_name = row["Primary Claimant's Name"]
        claimant_city = row["Claimant's City"]
        claimant_state = row['State']

        # print(city)


"""
~ use conditional logic to filter data ~
"""

with open('../data/lotto.csv', 'r', newline='') as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        county = row['County']
        retailer = row['Selling Retailer']
        address = row['Business Address']
        city = row['City']
        date_claimed = row['Date Claimed']
        game = row['Game']
        amount = row['Prize Amount']
        claimant_name = row["Primary Claimant's Name"]
        claimant_city = row["Claimant's City"]
        claimant_state = row['State']

        if city.strip() == 'KINGSTON':
            print(row)




"""
~ writing to a CSV ~

Unsurprisingly, you can also write to a CSV (use 'w' mode). The `csv.writer` object's `writerow()` method expects a list; the `csv.DictWriter`'s method expects a dictionary.
"""

# write lists
with open('test-writer.csv', 'w') as outfile:
    writer = csv.writer(outfile)

    headers = ['name', 'age', 'profession']

    writer.writerow(headers)

    journos = [
        ['Frank', 52, 'Reporter'],
        ['Sally', 37, 'Editor'],
        ['Pat', 41, 'Producer']
    ]

    for journo in journos:
        writer.writerow(journo)


# write dictionaries
# notice that you have to specify the headers when you
# create the `DictWriter` object -- you pass a list to
# the `fieldnames` keyword argument -- and they have
# to match exactly the keys in the dictionaries
# of the rows you're writing out
with open('test-dictwriter.csv', 'w') as outfile:

    headers = ['name', 'age', 'profession']

    writer = csv.DictWriter(outfile, fieldnames=headers)

    writer.writeheader()

    journos = [
        {'name': 'Frank', 'age': 52, 'profession': 'Reporter'},
        {'name': 'Sally', 'age': 37, 'profession': 'Editor'},
        {'name': 'Pat', 'age': 41, 'profession': 'Producer'}
    ]

    for journo in journos:
        writer.writerow(journo)


"""
EXERCISES:
- Open the lotto.csv file and loop over the rows -- print only the records where the claimant's state is NY
- Create a couple of rows of data -- anything, doesn't matter -- and write them out to a CSV file
"""
