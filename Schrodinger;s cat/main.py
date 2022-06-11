from random import choice

while True:
    left = choice([True, False])
    right = False if left else True

    Choice = input('Is the cat to the left or right?[L] [R] \t')

    if Choice:
        if Choice == 'L' and left:
            print('You won!')
            continue
        if Choice == 'L' and not left:
            print('You Lost!')
            continue
        if Choice == 'R' and right:
            print('You won!')
            continue
        if Choice == 'R' and not right:
            print('You Lost!')
            continue
