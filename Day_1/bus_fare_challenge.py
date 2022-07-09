''' Bus Fare Challenge Module 
Prints the date, day and fare charges
'''


import datetime


date = datetime.date.today()
day = today.strftime('%a')

if int(today.strftime('%w')) == 6:
    fare = 60

elif int(today.strftime('%w')) == 0:
    fare = 80

else:
    fare = 100

print('Date: {}\nDay: {}\nFare: {}'.format(date, day, fare))
