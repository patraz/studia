user_dict = {
    'majki': '1234',
    'Kamil001': '1244',
    'Rafcio': '12134',
    'Betty': '12dd34'
}

def has_passwd_cap_and_small_letter(password):
    if password.upper() != password and password.lower() != password:
        return True
    else:
        print(f"nie znaleziono duzej badz małej litery")
        return False


def pass_has_digit(password):
    if password.isalnum():
        return True
    else:
        print('brak liczby')
        return False


def passwd_has_special_character(password):
    if len(set(password) & secial_characters):
        return True
    else:
        print("Brak znaku specjalnego")
        return False

def is_passwd_correct(password):
    if passwd_has_special_character(password) and has_passwd_cap_and_small_letter(password) and pass_has_digit(password):
        return True
    return False



digits = set('0123456789')
secial_characters = set('.,/;:!@#$%\'\"\\')

def find_available_name(username):
    while is_username_available(suggest_username(username)) is False:
            username = suggest_username(username)
    username = suggest_username(username)
    print(f'Dostępna nazwa to {username}')
    return username

def user_add(username):
    while True:
        passwd1 = input('podaj hasło ')
        if is_passwd_correct(passwd1):
            passwd2 = input('podaj jeszcze raz hasło ')
        
            if passwd1 == passwd2:
                user_dict[username] = passwd1
                print(f'{username} dodany do listy użytkowników')
                break


def is_username_available(username):
    if username not in user_dict:
        print('nazwa dozwolona')
        return True
    else:
        print('nazwa NIEdozwolona')
        return False

def suggest_username(username):
    return username + '1'
