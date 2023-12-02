from f_do_domowe import user_dict,find_available_name, user_add, is_username_available, suggest_username

# Zadanie domowe:
# dana jest lista użytkowników
# user_list = ['majki', 'Kamil001', 'Rafcio', 'Betty']
# - program pyta o wprowadzenie nowego użytkownika
# - jeśli nazwa użytkownika jest zajęta program prosi o ponowne wprowadzenie nazwy bądź proponuje swoją podobną nazwę
# - po wprowadzeniu uzytkownika, program 2 razy prosi o hasło
# - po dwukrotnie wprowadzonym takim samym haśle, uzytkownik zostaje dodany do listy użytkowników, a jego hasło jest zapisane w drugiej liście




username = input('podaj nazwe uzytkownika   ')

while True:
    if is_username_available(username):
        user_add(username)
        break
    else:
        username = find_available_name(username)
        decission = input(f'Chcesz użyć nazwę {username} (1), czy wpisać swoją? (2)   ')
        if decission == '1':
            user_add(username)
            break
        else:
            username = input('podaj nazwe uzytkownika   ')


print(user_dict)





