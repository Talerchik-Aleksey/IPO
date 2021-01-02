#open
readin = open('input.txt', 'r')
output = open('output.txt', 'w')

data = readin.readlines() # read one line
data.sort() # sort line
data = [line.rstrip() for line in data] # delete '/n'
for i in range(len(data)):
    print(data[i], end='\n', file=output) # write answer
    
#close()
readin.close()
output.close()
