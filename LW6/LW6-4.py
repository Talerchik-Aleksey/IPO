a, b = map(int, input('Enter n and m: ').split())


mas = []
for i in range(a):
    mas.append([])
    for c in input().split():
        mas[i].append( int(c) )
index, jindex = 0, 0, 0, 0
max = mas[0][0]
for i in range(a):
    for j in range(b):
        if max < mas[i][j]:
            max = mas[i][j]
            index = i + 1
            jindex = j + 1
print(index, jindex,' - i and j')
