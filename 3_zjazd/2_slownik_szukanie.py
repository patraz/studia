browser_speed = {'Chrome': 100, 'Opera': 23, 'Firefox': 76, 'Safari': 58}

print(list(browser_speed.keys())[0])  #klucze
print(list(browser_speed.values())) #wartości
print(list(browser_speed.items())) # (klucze,wartosci) lista krotek

print(list(browser_speed.keys())[list(browser_speed.values()).index(76)]) # znajduje key po value, w tym przypadku znajduje Firexfox po 76
