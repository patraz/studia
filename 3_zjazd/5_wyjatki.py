
def can_be_int(data):
    try:
        data = int(data)
        return True
    except ValueError:
        return False
    
x = input('Podaj liczbę: ')
if can_be_int(x):
    print('liczymy dalej ')
else:
    print('Podales zla liczbe')


def convert(data):
    try:
        data = int(data)
        print('Skonwertowano do int')
        return data
    except ValueError:
        print('Zostanie string')
        return data