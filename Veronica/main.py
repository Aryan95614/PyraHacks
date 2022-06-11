import time
import random

print('Hi, I am Veronica!')
time.sleep(1)
a = input('\nWhat is your name?\t')
Places = ["Wild Coast, South Africa.", "The sunrise at Kawah Ijen, Indonesia", "Solo camping in Utah, USA", "Tofo, Mozambique.", "The Ring Road and northern lights, Iceland", "The Annapurna Circuit, Nepal", "Komodo National Park, Indonesia.", "Torres del Paine, Chile", ]

choice = input(f'Hello {a}, do you like {random.choice(Places)}?[y][n]')

if choice == 'y':
    print(f'I like that place but {random.choice(Places)}, no {a}?')
if choice == 'n':
    print(f"What are you saying{a}! That's my favourite place!")
