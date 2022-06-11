import math


a = round(float(input()), 2)
b = round(float(input()), 2)
c = round(float(input()), 2)

side = (a+b+c)

answer = side * (b+c-a)* (b-c+a)* (a+b- c)

answer = math.sqrt((answer/16))
print(f'Your answer is:\t', answer)