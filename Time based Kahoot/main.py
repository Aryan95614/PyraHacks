
print('This is the Avengeful Aryan Kahoot, have fun! Your score is currently 0!')

score = 0

intput = lambda x: int(input(x))

print('First Question: If John Conner did not create Human Resistance, would there be another individual like John Conner?')

print('[1] No, it would actually make a timeline where the Terminators win')
print('[2] Yes, as Causal Relationships transcribe the events throught the person and not vice versa')
print('[3] All of the Above')
print('[4] None of the Above')

choice = intput('What is your choice?:\t')

if choice == 2:
    score += 20
    print(f'Yay your score is now {score}')

else:
    print('Better Luck next time')



print('----------------------------------------------------------')
print('Second Question: Is power rule a part of Calculus?')

print('[1] No, it is apart of Differnetial Calculus but does not appear in integration calculus')
print('[2] Yes, as its how to take derivatives')
print('[3] All of the Above')
print('[4] None of the Above')

choice = intput('What is your choice?:\t')

if choice == 3:
    score += 30
    print(f'Yay your score is now {score}')

else:
    print('Better Luck next time')

print('----------------------------------------------------------')
print('Third Question: Is Python a General Purpose Language?')

print('[1] No, it is apart the Dynamic Paradigm')
print('[2] Yes, as its purpose can be utilized in different roles')
print('[3] All of the Above')
print('[4] None of the Above')

choice = intput('What is your choice?:\t')

if choice == 2:
    score += 40
    print(f'Yay your score is now {score}')

else:
    print('Better Luck next time')

print(f'Your score is {score}')