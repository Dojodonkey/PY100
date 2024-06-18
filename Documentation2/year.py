'''
The Python documentation for the
 datetime module provides two attributes
 to retrieve the year from a date or datetime object:
 year and isocalendar.

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

What is the difference between the year attribute
 and the isocalendar method?
'''

#isocalendar() returns a tuple object with three components: 
#(year, week, weekday) based on the gregorian calendar. 

from datetime import date

today_iso =  date(2024, 6, 18).isocalendar()

print(today_iso)

#the year attr returns the year. 

today = date.today()

today_year = today.year

print(today_year)

