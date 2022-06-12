
print('This is to help people with Anxiety!--------------')

score = 0

choice = input('Have you felt liek you need ot complete an objective?[y][n]\t')

if choice == 'y':
    print('Please contact +1 866-681-6578')
    score += 20

choice1 = input("Have you looked at something and felt anxious?[y][n]\t")

if choice1 == 'y':
    print('Please contact 1-866-585-0445')
    score += 15

choice2 = input("Did you ever have any depression?[y][n]\t")

if choice2 == 'y':
    print('Please contact +1 (647) 800-1781')
    score += 15


if score > 29:
    print(' You have a likely chance of depression, please contact the numbers you have received.')

else:
    print(' You should be happy and optimistic!')