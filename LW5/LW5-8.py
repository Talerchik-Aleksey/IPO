import random
def main():
    lst = []
    
    for i in range(10):
        lst.append(random.randint(0, 10))
    print(lst)
    reiteration(lst)
    
def reiteration(lst):
    new_list = []
    
    for i in lst:
        if lst.count(i) > 1 and (i not in new_list):
            new_list.append( i )
    print(new_list)
main()
