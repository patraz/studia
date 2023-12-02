#petla while
# x= 0
# while x < 5:
#     print(x)
#     x += 1

# przykład 2

# age = int(input('ile masz lat? '))
# while age < 18:
#     print('za młody, spróbuj jeszcze raz')
#     age = int(input('ile masz lat? '))

# print('Welcome, masz dostep do treści')


# przykład 3
# zgadnij liczbę wylosowaną przez program
#if zgadniesz 2pkt
#if not 1pkt
#trzeba 5 pkt

import random

points = 0 
rundy = 1

while points < 5:
    num = random.randrange(1,10)

    print(f'trwa {rundy} runda')

    guess = int(input('zgadnij liczbę od 1-9  '))
    random_number = f'losowa liczba to {num}'

    if guess == num:
        points += 5
        print(random_number)
        print('zdobyłeś 5 pkt')
    elif abs(guess - num) == 1:
        points += 3
        print(random_number)
        print('zdobyłeś 3 pkt')
    else:
        points += 1
        print(random_number)
        print('zdobyłeś 1 pkt')
    rundy += 1
print('zdobyłeś 5 pkt')
