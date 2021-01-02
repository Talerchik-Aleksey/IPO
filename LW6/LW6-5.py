a, b = map(int, input().split())


mas = []
for i in range(a):
    mas.append([])
    for c in input().split():
        mas[i].append( int(c) )
new_mas = []
for i in range(b):
    new_mas.append([])
    for j in range(a):
        new_mas[i].append(mas[j][i])
print(new_mas)
for i in range(b):
    for j in range(a - 1, -1, -1):
        print(new_mas[i][j], end=' ')
    print()
