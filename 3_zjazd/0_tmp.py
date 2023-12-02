x = lambda a: a + 10
print(x(19))


def tax(income, no_of_children, savings = 0):
    return income * .2 + no_of_children * 0.95 + savings * 0.1