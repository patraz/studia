# main_pass = 1234
# second_pass = 2345

# while True:
#     password = int(input("podaj hasło:  "))
#     if password == main_pass:
#         break
#     elif password == second_pass:
#         age = int(input("podaj wiek:  "))
#         if age >= 18:
#             break
#         print('za młody, sorry')
#     else:
#         print('Złe dane, sorry')
# print('wchodzisz')


#program losuj liczbę od 1-100
#zgadujesz liczbe
#program mowi czy zgadnięta czy za mało czy ok 

import random

num = random.randrange(1,101)

while True:
    guess = int(input('zgadnij liczbę od 1-100  '))
    if guess == num:
        print('Brawo! Udało się')
        break
    elif guess > num:
        print('Za dużo, try again')
    elif guess < num:
        print('Za mało, try again')
        
    

