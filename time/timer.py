import time

# time based application

a, b, c = True, True, True
while True:
    g = input(' Do you want the time?[y]\t')
    if g == 'y':
        print(time.perf_counter())

    if time.perf_counter() > 2 and a:
        a = False
        print('Keep on going!')

    if time.perf_counter() > 20 and b:
        b = False
        print('Among us is a good game!')

    if time.perf_counter() > 10 and c:
        c = False
        print('Harambe is our savior')
