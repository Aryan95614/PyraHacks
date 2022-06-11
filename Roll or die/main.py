import random

dice_values = [1, 2, 3, 4, 5, 6]
balence = 0

while True:
    current = random.choice(dice_values)
    choice = input(f' Your balence is {balence} would you like to add {current}?[y][n]\t')

    if choice == 'y':
        balence += current

    if balence > 30:
        print('You lose!')
        break

    if balence == 30:
        print('You Win!')
        break
