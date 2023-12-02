#przeczytac plik
from funkcje_do_4 import no_of_words

with open('U2.txt', 'r') as file:
    content = file.read()

#wyczyscic dane

#znalezc liczbe slow
#znaklezc liczbe  roznych slow
#zapisac ilosc powtorzen kazdego slowa
print(no_of_words(content))
