def main():
    count_1, count_2, count_3 = 0, 0, 0
    for elem in list:
        if (elem <= 3) and ( elem >= 1):
            count_1 += 1
        if (elem <= 6) and ( elem >= 4):
            count_2 += 1
        if (elem <= 9) and ( elem >= 7):
            count_3 += 1
    print(count_1, count_2, count_3)

list = [1, 1, 3, 4, 3, 6, 7, 8, 7, 5, 7, 9, 9, 9, 8]
main()
