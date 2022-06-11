from itertools import permutations

name = input('What is your name?\t')

list = permutations(name)

for i in list:
    print(i)
