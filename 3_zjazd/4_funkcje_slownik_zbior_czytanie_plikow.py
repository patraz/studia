#przeczytac plik
from funkcje_do_4 import *

with open('U2.txt', 'r') as file:
    content = file.read()

#wyczyscic dane

#znalezc liczbe slow
#znaklezc liczbe  roznych slow
#zapisac ilosc powtorzen kazdego slowa
content = clean_text(content)
content = make_split(content)
print(f'ilość słów {no_of_words(content)}')
print(f'Liczba unikalnych słów {no_of_unique_words(content)}')

print(reps_of_words(content))