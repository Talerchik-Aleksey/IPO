import random

def main():
    lst = []

    for i in range(30):
        lst.append(random.randint(-100, 100))
    print(lst)
    sort(lst)
    
def sort(lst):
    new_list = []

    for i in lst:
        if (i > 0):
            new_list.append(i)
    multiplication(new_list)

def multiplication(new_list):
    print(new_list[0],' * ', new_list[2],' * ',new_list[5],' = ', new_list[0] * new_list[2] * new_list[5])

main()
