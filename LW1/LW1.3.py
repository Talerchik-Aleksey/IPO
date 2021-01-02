a = int(input())
b = int(input())
c = int(input())

p = float(0.5*(a+b+c))

s = p*(p-a)*(p-b)*(p-c)

s = s**0.5

print(s)
