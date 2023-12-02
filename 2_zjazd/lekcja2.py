# pomidory kosztują 3zł sztuka. Ale w 3-paku, 3 pomidory razem kosztują 80% ceny

# program pyta ile pomidorów chcemy kupić i zwraca najniższą cenę


#werjsa 1
price_per_tomato = 3
no_of_tomatoes = int(input('Ile pomidorów chcesz kupić?  '))
no_of_3packs = no_of_tomatoes // 3
no_of_single_tomatoes = no_of_tomatoes % 3
total_price = no_of_3packs * 3 * price_per_tomato * 0.8 + no_of_single_tomatoes*3

print(f'zaplacisz {total_price}zł')

#petla while
x= 0
while x < 5:
    print(x)
    x += 1

