import sys, random, os
import pygame

pygame.init()

image = pygame.transform.scale( pygame.image.load(os.path.join('assets', 'man (1).png')),(64, 64))
gameover = False
class Player:

    def __init__(self):
        self.name = input('What is the name of this person?:\t')
        self.age = int(input('What is the age of this person?:\t'))
        self.pronouns = input('What are the pronouns of the individual?\t')

    def print(self):
        print(f'The name is {self.name}, the age is {self.age}, and the pronouns is {self.pronouns}')

people= []
condition = True
while condition:
    choice = int(input('Add someone?[1] or Look at Someone[2] or quit[3]: \t'))
    if choice == 1:
        people.append(Player())
    if choice == 2:
        person = input('Who is the person? [Insert Number here]?')
        try:
            people[person].print()
        except Exception as e:
            print(e)
    if choice == 3: condition = False


if not condition:
    Number = len(people)
    win = pygame.display.set_mode((800, 800))

    lists = []

    for i in range(len(people)):
        lists.append([pygame.transform.scale(image, (64+ people[i].age, 64+ people[i].age)), (random.randint(100, 700), random.randint(100, 700)) ])
    while not gameover:
        win.fill((225, 225, 225))

        for i in range(len(lists)):
            win.blit(lists[i][0], lists[i][1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()
