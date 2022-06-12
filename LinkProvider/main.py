from random import choice
import sys

while True:
    print('\n------------------This gives links: ------------')

    choices = input('Do you like Comedy[1], Horror[2], Thriller[3], Popular[4], Special[5], Quit[6]')

    special = ['https://www.youtube.com/watch?v=g4SjaZb1AIM', 'https://www.youtube.com/watch?v=B_tTymvDWXk', 'https://www.youtube.com/watch?v=3Yd7ocEaZYc', 'https://www.youtube.com/watch?v=FIjV5mWBFUw', 'https://www.youtube.com/watch?v=ykpWl-gXZ6s']
    if choices == 1:
        answer = input('Do you want to watch Shrek[1] or Tom and Jerry[2]')
        if answer == 1:
            print('https://www.youtube.com/watch?v=qgI10n5ZxwQ&list=PLJQFXjaPhq6UNZQdPVyz0eaHUCd06VIer')
        if answer == 2:
            print('https://www.youtube.com/watch?v=wywYnajCgaU')

    if choices == 2:
        answer = input('Do you want to watch Anabelle[1] or Scary Doll[2]')
        if answer == 1:
            print('https://www.youtube.com/watch?v=Q6XvFKYWWSc')
        if answer == 2:
            print('https://www.youtube.com/watch?v=Z1qoWipSXcs')

    if choices == 3:
        answer = input('Do you want to watch Deep Water[1] or Memory[2]')
        if answer == 1:
            print('https://www.youtube.com/watch?v=qW-TQAPooCA')
        if answer == 2:
            print('https://www.youtube.com/watch?v=palAASzEsZI')

    if choices == 4:
        answer = input('Do you want to watch Shrek[1] or Tom and Jerry[2]')
        if answer == 1:
            print('https://www.youtube.com/watch?v=qgI10n5ZxwQ&list=PLJQFXjaPhq6UNZQdPVyz0eaHUCd06VIer')
        if answer == 2:
            print('https://www.youtube.com/watch?v=wywYnajCgaU')

    if choices == 5:
        print(choice(special))

    if choices == 6:
        sys.exit()

