# użytkownik wprowadza osoby
# imie, nazwisko, mail

# program pyta czy wprowadzić kolejną osobę

#po zakonczeniu wprowadzania program wypisuje
# ile jest kobiet
# ile osob w gmail


users = []
kobiety = 0
gmail = 0

while True:
    name = input('dodaj imie osoby   ')
    surename = input('dodaj nazwisko osoby   ')
    mail = input('dodaj mail osoby  ')
    user = [name, surename, mail]
    users.append(user)
    next = input('Czy chcesz dodać następną osobę? T/N:  ')
    if next == 'N':
        break

for user in users:
    user_name = user[0]
    user_mail = user[2]

    if user_name[-1] == 'a':
        kobiety += 1
    if 'gmail' in user_mail:
        gmail +=1

print(users, kobiety, gmail)

