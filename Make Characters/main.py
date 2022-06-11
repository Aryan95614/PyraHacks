import sys

class Player:

    def __init__(self):
        self.name = input()
        self.age = int(input())
        self.pronouns = input()

    def print(self):
        print(f'The name is {self.name}, the age is {self.age}, and the pronouns is {self.pronouns}')

people= []
while True:
    choice = int(input('Add someone?[1] or Look at Someone[2] or quit[3]'))
    if choice == 1:
        people.append(Player())
    if choice == 2:
        person = input('Who is the person? [Insert Number here]?')
        try:
            people[person].print()
        except Exception as e:
            print(e)
    if choice == 3: sys.exit()