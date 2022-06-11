amounts = [500] * 4
Categroies = ['Whats 1 + 1?', 'How are you?', 'Minecraft has 256 blocks[y]', 'Amogus is supreme']
balence = 0

while True:

    choice = int(input(f'You have ${balence}. What is your choice, 1- 4: \t'))
    if Categroies:
        if choice == 1:
            answer = int(input(f"What is {Categroies[0]}"))
            if answer == 2: balence += 500;Categroies.remove(Categroies[0])

        elif choice == 2:
            print(f"What is {Categroies[0]}")
            print('Stay Positive, times are tough, persevere!')
            balence += 500
            Categroies.remove(Categroies[1])

        elif choice == 3:
            if input(f"What is {Categroies[0]}[y][n]") == 'n':
                balence += 500
        else:
            if input(f"What is {Categroies[0]}[y][n]") == 'y':
                balence += 2000
    else: print(f' Lmao thx for playing, your balence is ${balence}')
