def main():
    list, elem, elem1 = [], 0, 0

    for elem in list_1:
        for elem1 in list_2:
            if elem == elem1:
             list.append(elem)

    print(list)

list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
main()
