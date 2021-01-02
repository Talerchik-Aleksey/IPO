import math

a = int(input())
b = int(input())
c = int(input())
k = int(input())

print ('1. ', float((a**2/b**2+c**2*a**2)/(a+b+c*(k-a/b**3))+c+(k/b-k/a)*c))

d = int(input())
print ('2. ', float((a**2-b**3-c**3*a**2)*(b-c+c*(k-d/b**3))-(k/b-k/a)*c)**2-20000)
print ('3. ', math.ceil(float(math.fabs(1-a*b**c-a*(b**2-c**2)+(b-c+a)*(12+b)/(c-a)))))

f = int(input())
print ('4. ', math.ceil(float(math.fabs(a-b*c*d**3+(c**5-a**2)/a+f**3*(a-213)))))
