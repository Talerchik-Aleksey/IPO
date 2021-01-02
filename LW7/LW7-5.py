massiv = [int(s) for s in input().split()]
vstrecha = set()
for num in massiv:
    if num in vstrecha:
        print('YES')
    else:
        print('NO')
        vstrecha.add(num)
