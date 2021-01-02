import random
def boundaries():    
    first_bound = int(input('Enter boundaries(min): '))
    second_bound = int(input('Enter boundaries(max): '))
    main(first_bound, second_bound)

def main(first_bound, second_bound):
    lst, count = [], 0

    for i in range(20):
        lst.append(random.randint(0, 10))
    print(lst)
    for i in lst:
        if (i >= first_bound) and (i <= second_bound):
            count += 1
            
    print(count,' - min < x < max')

boundaries()
