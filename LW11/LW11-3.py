class Dete(object):
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
    
    def sqer(self):
        print (2*(self.a*self.b + self.a*self.c +self.b*self.c))
    def v(self):
         print(self.a * self.b * self.c)
               

a = input('a: ')
b = input('b: ')
c = input('c: ')

if __name__ == "__main__":
    dete = Dete(a, b, c)
    dete.sqer()
    dete.v()
