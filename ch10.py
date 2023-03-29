import random as r
from datetime import date
a = int(input('set a max number to find random value : '))
print(r.randrange(a))
now = date.today()
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

