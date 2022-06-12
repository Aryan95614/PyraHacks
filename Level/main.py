
print('This is to help people with depression!--------------')

score = 0

choice = input('Have you felt down lately, like you get good achievements?[y][n]\t')

if choice == 'y':
    print('Please contact +1 833-456-4566')
    score += 20

choice1 = input("Have you looked at the world and think that it doesn't matter?[y][n]\t")

if choice1 == 'y':
    print('Please contact +1 707-998-8410')
    score += 15

choice2 = input("Do you have any prior mental disabilities?[y][n]\t")

if choice2 == 'y':
    print('Please contact +1 (647) 800-1781')
    score += 15


if score > 29:
    print(' You have a likely chance of depression, please contact the numbers you have received.')

else:
    print(' You should be happy and optimistic!')