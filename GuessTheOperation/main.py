from random import randint, choice

sum = lambda x, y: x+ y
minus = lambda x, y: max(x, y)-min(x, y)
multiply = lambda x, y: x* y
divide = lambda x, y: max(x, y)// min(x, y)

while True:
    a = randint(2, 5)
    b = randint(2, 5)

    List = [[1, sum(a, b)],
            [2, minus(a, b)],
            [3, multiply(a, b)],
            [4, divide(a, b)]]

    Lis = choice(List)
    thing = Lis[1]
    correct = Lis[0]
    answer = int(input(f'The amount is {thing} and the numbers are {a, b}, Add [1], subtract [2], Multiply [3], Floor Divide[4]:\t'))
    if Lis[0] == answer:
        print('You are correct!!!')
    else:
        print('You Lost')




