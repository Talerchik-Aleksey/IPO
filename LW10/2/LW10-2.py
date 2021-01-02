with open('input.txt', 'r') as readin:	 	#open input.txt for read (readin)
    mass = []
    full = readin.read()
    for i in full.split():
        mass.append(int(i))
with open('output.txt', 'w') as output: 	#open output.txt for write (output)
    print(max(mass), file=output)
    print(min(mass), file=output)

#https://pythonworld.ru/osnovy/with-as-menedzhery-konteksta.html - with ... as
