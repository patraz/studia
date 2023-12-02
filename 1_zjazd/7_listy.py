# x = 'f,f,f,f,s,f,a,d'

# l = x.split(',')
# print(l)

# l.pop('f')

# del l[0:5]

# print(l)

sample_list = [5, 7.5, 12, 14, 23, 36, 45, 3433, 23, 44]
data_list = []
second_data_list = []

#program który weżmiel listę samplę list
#zapisze listt parzy

# for x in sample_list:
#     if x % 2 == 0:
#         data_list.append(x)
#     else:
#         second_data_list.append(x)


x = 0

while x < len(sample_list):
    if sample_list[x] % 2 == 0:
        data_list.append(x)
    else:
        second_data_list.append(x)
    x +=1

print(data_list)


