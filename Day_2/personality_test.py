''' Bookshop Personality Test Module'''


import datetime


month = datetime.datetime.now().strftime('%B')
books_purchased = -1
while books_purchased < 0:
    books_purchased = int(input("How many books have you purchased in "+ month +"?: " ))

awards = {0:0, 1:6, 2:16, 3:32, 4:60}

if books_purchased > 4:
    print("Points awarded: {}".format(awards[4]))
else:
    print("Points awarded: {}".format(awards[books_purchased]))
