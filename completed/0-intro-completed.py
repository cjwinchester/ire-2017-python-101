"""
~ printing things~

Use the `print()` function to print things to your console
"""

print('hello')
print('hello', 'IRE')
print('hello' + ' IRE')
print('i am', 32, 'years old')


"""
~ assigning variables ~

Use = to assign values to variables for later use.
"""

my_name = 'Cody'
print(my_name)

my_age = 22 + 10
print(my_age)

my_age_in_10_years = my_age + 10
print(my_age_in_10_years)


"""
~ basic data types: strings ~

Anything sandwiched between two quotes -- single or double, doesn't matter as long as they match.
"""

a_string = 'hello, i am a string'
another_string = "hello, i am another string"
an_escaped_string = 'hello, i\'m a string with an escaped apostrophe'


"""
~ basic data types: integers ~

A whole number.
"""

my_age = 32
my_age_10_years_ago = my_age - 10


"""
~ basic data types: floats ~

A number with a decimal.
"""

pct_of_whole = 45.6


"""
~ basic data types: booleans ~
 
True or False -- often used to test conditions. Always title case, never in quotes.
"""

my_boolean = True
my_other_boolean = False


"""
~ basic data types: lists ~

A collection of items inside square brackets. You can get the number of items in a list using the `len()` function.
"""

my_list = [1, 2, 3, 'hello', True, ['a', 'b', 'c']]
my_list_count = len(my_list)

print('There are', my_list_count, 'items in my list')

# to access items, use bracket notation and the index number
# counting in Python starts at zero,
# so to get the first item in a list, use [0]

first_item = my_list[0]
print(first_item)


"""
~ basic data types: dictionaries ~

Maps keys to values inside curly brackets.
NOTE: Dictionaries don't keep track of order.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3}

# to access items in a dictionary, you can
# use bracket notation and the key

print(my_dict['a'])


"""
~ type() ~

You can check the type of a thing with the `type()` function.
"""

print(type(43))
print(type(32.0))
print(type('True'))
print(type(True))
print(type([1, 2, 3]))
print(type({'a': 1, 'b': 2, 'c': 3}))


"""
~ dir() ~

You can check the attributes and methods of a thing with the `dir()` function.
"""

print(dir(43))
print(dir(32.0))
print(dir('True'))
print(dir(True))
print(dir([1, 2, 3]))
print(dir({'a': 1, 'b': 2, 'c': 3}))


"""
~ string methods: concatenating/formatting ~

A simple way to combine strings is `+`; a more advanced way that supports more data types is `format()`.
https://pyformat.info/
"""

my_string = 'Hello' + ' IRE!'
my_other_string = '{} My name is John Doe.'.format(my_string)
print(my_other_string)


"""
~ strip whitespace from strings ~

Use `strip()` to strip whitespace characters from either side of a string.
"""

my_ugly_string = '          hello       '
my_pretty_string = my_ugly_string.strip()


"""
~ join a list together into a string ~

Sometimes you want to join the string elements of a list together.
"""
month = '06'
day = '11'
year = '1985'

date_list = [year, month, day]

joined_date = '-'.join(date_list)
print(joined_date)


"""
~ `for` loop to iterate over a list ~

If you want to do something to each item in a list (or other kind of iterable), you can use a `for` loop.

NOTE the indentation on subsequent lines.
"""

my_word_list = ['hello', 'IRE', 'how', 'are', 'you']

for word in my_word_list:
    print(word)


"""
~ replace parts of strings ~

Use `replace()` to replace parts of a string with something else.
(NOTE: You can chain string functions together.)
"""
string_1 = 'Wal-Mart Corp.'
string_2 = 'Wal-Mart Corp., Inc.'
string_3 = 'WalMart'

string_1_clean = string_1.replace(' Corp.', '') \
                         .replace(', Inc.', '') \
                         .replace('WalMart', 'Wal-Mart')



"""
~ conditional logic ~

Just like in Excel, you can use conditional logic (IF [something], DO [thing A], else IF [other thing], DO [thing B], etc.)

NOTE the indentation on subsequent lines
"""

date_string_to_test = '2000-01-01'

# slice out the year and use the `int()` function
# to turn the string into an integer
year = int(date_string_to_test[:4])

if year < 2000:
    print('old and busted')
elif year == 2000:
    print('the start of a new millenium!')
else:
    print('new hotness')


"""
~ importing modules ~

You can import built-in Python libraries, third-party libraries and your own scripts
"""

import csv
import requests
import my_cool_vars as mcv

print(mcv.ire_2017_location)
print(mcv.ire_2017_year)

"""
EXERCISES:
- Create a list of strings of ingredients for a salsa recipe and assign it to the variable `salsa_list`
- Create a dictionary with the following key/value pairs and assign it to the variable `salsa_dict`:
    - 'recipe_name': a string that's the name of your salsa recipe
    - 'ingredients': whatever variable you saved your list of ingredients as
    - 'heat_level': an integer representing how hot your recipe is
- perform a logical test to print out whether your recipe's heat level is above 10, under 10 or exactly 10
"""
