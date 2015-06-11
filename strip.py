import re
s = """ DATA GOES HERE
"""
numbers = re.findall( r'\d+\.*\d+%',s)
every_other_number = numbers[::2]
for number in every_other_number:
    number = number[:-1]
    print number,

