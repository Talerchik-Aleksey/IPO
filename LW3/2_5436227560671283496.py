num = int(input())

a = 0
b = 0

while num > 0:
    if num % 2 == 0:
        a += 1
    else:
        b += 1
    num = num // 10

print(a, b)
