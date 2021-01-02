import io

with io.open('input.txt','r', encoding='utf-8') as file:
    file = file.read().splitlines()
        
with open('output.txt', 'w') as output: 	#open output.txt for write (output)
    for i in file:
        for j in i.split():
            if (j.isdigit() == True) and int(j) < 40:
                print(i, file=output)

#https://pythonworld.ru/osnovy/with-as-menedzhery-konteksta.html - with ... as
