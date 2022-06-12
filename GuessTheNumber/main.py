from random import choice
import sys

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
score = 5
things = False
while True:
    Random = choice(numbers)
    thing = int(input(f'Hello, a random number was chosen, please type in a number, your score is {score}:\t'))
    if thing == int(Random):
        score += 1
        print(f'You win, your score is {score}, the number was {Random}')

    else:
        print(f'You lose, your score is {score}')

    if score == 5 and not things:
        things = True
        print('Congrats, now the other part of the game, now you can select the numbers, split by comma:\t')
        numbers = input(' Numbers: \t').split(', ')
