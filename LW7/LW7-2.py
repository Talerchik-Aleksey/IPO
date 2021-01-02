def repeat_finder():   
    x = set()
    for elem in lst:
        if lst.count(elem) >= 2:
            x.add(elem)
    return x

lst = [1,2,3,4,5,5,10,2,10,10]
print(repeat_finder())
