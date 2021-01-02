import random

def main():
    lst = []

    for i in range(30):
        lst.append(random.randint(-100, 100))
    print(lst)
    min_and_max(lst)
    
def min_and_max(lst):
    mai, mii,index = 0, 0, 0

    for i in lst:
        if i > lst[mai]:
            mai = index
        if i < lst[mii]:
            mii = index
        index += 1
    print(lst[mai],' - max', lst[mii],' - min')
    change(mii,mai, lst)
    
def change(mii, mai, lst):
    lst[mii], lst[mai] = lst[mai], lst[mii]
    print(lst)
main()
