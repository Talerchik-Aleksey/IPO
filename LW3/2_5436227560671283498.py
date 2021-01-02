num1 = float(input())
num2 = float(input())
c = 1

print(' + - plus, - - minus, * - multiply, / - share,\n ^ - elevate, root - root, bin - bin')
count = input('Please enter operator: ')

while count != "0":
    if count == "+":
        print(num1 + num2)
    if count == "-":
        print(num1 - num2)
    if count == "*":
        print(num1 * num2)
    if count == "/":
        print(num1 / num2)
    if count == "^":
        print(num1 ** num2)
    if count == "root":
        print(num1**0.5, num2**0.5)
    if count == "bin":
        int1 = int(num1)
        int2 = int(num2)
        print(bin(int1), bin(int2))

        
    count = input('Repeat operator or exit(0)? ')
