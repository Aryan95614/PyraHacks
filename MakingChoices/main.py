from random import choice
import sys

print('-------------------Double or anything!!!-------------------\n')

choices = ['Would you like $20?',
           'Would you like $500?',
           'Would you like a Jacuzzi?',
           'Would you like to have a [Small] Mansion?',
           'Would you like to have a [Medium] Mansion?',
           'Would you like to have a [Large] Mansion?',
           'Would you like a series of iphones?']

while True:
    thing = choice(choices)
    print(thing)
    Answer = input('Do you want to accept this offer?:[y][n]\t')
    if Answer == 'y':
        print(f'Great you selected {thing[14:-1]}')
        sys.exit()
    elif Answer == 'n':
        choices.remove(thing)
        print('\n Great! Now you can select other things')