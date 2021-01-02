import random
class Main():
    def __init__(self,s1,s2):
        self.size = s1
        self.matrix = [[round(random.uniform(0,10), 2) for y in range(s1)] for x in range(s2)]
    def prnt(self):
        for im in range(self.size):
            print(*self.matrix[im])

class Choose(Main):
    def m(self):
        self.lable = int(input('1 - (+, -), 2 - (+=, -=), 3 - (!=, =), 4, 5 - ([i][j]): \n'))
        
W1 = Choose(5, 5)
W1.prnt(); W1.m()
