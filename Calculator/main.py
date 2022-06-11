import math

while True:
    first = float(input())
    second = float(input())
    total = 0
    c = input("What is your operation? [+] {-} (x) [/] [Trig] ")

    if c:
        if c == '+':
            print(first + second)
        if c == '-':
            print(max(first, second) - min(first, second))
        if c == 'x':
            print(first * second)
        if c == '/':
            print(max(first, second) / min(first, second))
        if c == 'Trig':
            print('The sin of x is ', round(math.sin(first), 2))
            print('The cos of x is ', round(math.cos(first), 2))
            print('The tan of x is ', round(math.tan(first), 2))
            print('The sec of x is ', round(1 / math.sin(first), 2))
            print('The csc of x is ', round(1 / math.cos(first), 2))
            print('The cot of x is ', round(1 / math.tan(first), 2))

            print('The sin of x is ', round(math.sin(second), 2))
            print('The cos of x is ', round(math.cos(second), 2))
            print('The tan of x is ', round(math.tan(second), 2))
            print('The sec of x is ', round(1 / math.sin(second), 2))
            print('The csc of x is ', round(1 / math.cos(second), 2))
            print('The cot of x is ', round(1 / math.tan(second), 2))

    print('------------------ Thank you for Playing! ----------------------')
