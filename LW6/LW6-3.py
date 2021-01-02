a, b = 5, 6
def main():
    mas = []
    for i in range(a):
        mas.append([])
        for j in range(b):
            mas[i].append(i*j)
    print_list(mas)
        
def print_list(mas):
    for i in range(a):
        for j in range(b):
            print(mas[i][j], end=' ')
        print()

main();
