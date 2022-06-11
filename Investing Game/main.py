
from random import randint

Intial = 100
Stock = 20
ShareHolding = 0

while True:
    print(f" You have {Intial} in trading volume and {Stock} worth in stock you are holding {ShareHolding}")
    Stock += randint(-5, 5)
    print(f" The stock price is {Stock} today, would you like to invest?[y]")
    if input() == 'y':
        Intial -= Stock
        ShareHolding += Stock

    else:
        Intial += Stock
        ShareHolding -= Stock
