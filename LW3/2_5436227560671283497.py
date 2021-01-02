num = int(input())

s = 0
p = 1

while num > 0:
    c = num % 10
    s += c
    p *= c
    num = num // 10

print('Sum = ',s,' Com = ', p)
