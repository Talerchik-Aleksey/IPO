def main():
    for i in range(len(list)):
        for j in range(len(list[i])):
            if i == j:
                list[i][j] = 1
            elif i < j:
                list[i][j] = 0
            else:
                list[i][j] = 2
    new_list(list)
    
def new_list(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j], end=' ')
        print()

list = [[1, 2, 3, 4], [4, 3, 2, 1], [3, 4, 5, 6], [1, 1, 1, 1]]
main()
