st = input('Enter string: ')
string = st[(len(st) + 1) // 2:] + ' ' + st[:(len(st) + 1) // 2]
print(string)
