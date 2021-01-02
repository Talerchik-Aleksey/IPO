with open('input.txt', 'r') as readin:	 	#open input.txt for read (readin)
    mass = []
    readin = readin.read().splitlines()
        
with open('output.txt', 'w') as output: 	#open output.txt for write (output)
    words, letters = 0, 0
    print('Input file contains:', file=output)
    for i in readin: # line
        for j in i: #letters
            if j != ' ' and j != '.':
                letters += 1
        for j in i.split(): #words
            words += 1
    print(letters,' - letters\n',words,' - words\n',len(readin),' - lines\n', file=output)
    
#https://pythonworld.ru/osnovy/with-as-menedzhery-konteksta.html - with ... as
