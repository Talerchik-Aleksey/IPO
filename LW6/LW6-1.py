def main (list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j], end=' ')
        print()

list = [[1, 2, 3], [3, 2, 1]]
main (list)
