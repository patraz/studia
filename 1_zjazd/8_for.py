

# ile do listy




#czy dane słowo jest palindromem
# czy pisze isę tak samo od konca i od poczatku 

word = 'kaninjak'


def palindrom_check(word):
    if word == word[::-1]:
        return True
