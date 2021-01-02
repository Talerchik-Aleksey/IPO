import random

def lst(a, b):
    lst_new = []
    for i in range(10):
        lst_new.append( random.randint( a, b ) )
    return lst_new

a, b = 0, 5
tuple_one = tuple( lst(a, b) )
b = -5
tuple_two = tuple( lst(b, a) )
tuple_three = tuple_one + tuple_two
print(tuple_three)
print(tuple_three.count(0),' - 0 in tuple №3')
