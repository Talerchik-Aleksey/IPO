import math
class Geometry:
    def _init_(self,name):
      self.name=name
    def showinfo(self):
        print('это ' + self.name)
class ell(Geometry):
    A, B = 5, 5
    def _init_(self,name,A,B):
        super().init_(name) # https://habr.com/ru/post/62203/?_ga=2.138387703.658467488.1609257651-1626585611.1607851447
        self.A=A
        self.B=B
    def ok(self):
        print('площадь эллипса: ',(math.pi*self.A*self.B))
    def pk(self):
        print('периметр эллипса: ',(2*math.pi*math.sqrt((self.A**2+self.B**2)/2)))
class kv(Geometry):
    R=3
    l=7
    def _init_(self,name,R,l):
        super().init_(name) # https://habr.com/ru/post/62203/?_ga=2.138387703.658467488.1609257651-1626585611.1607851447
        self.h=h
        self.R=R
    def oko(self):
        print('площадь квадрата: ',(self.R*self.l))
    def pko(self):
        print('периметр квадрата: ',((self.R+self.l)*2))
class tr(Geometry):
    K=5
    L=4
    H=2
    F=4
    O=5
    def _init_(self,name,K,L,H,F,O):
        super().init_(name)
        self.K=K
        self.L=L
        self.H=H
        self.F=F
        self.O=O    
    def pt(self):
        print('площадь трапеции: ',(1/2*(self.K+self.L)*self.H))
    def ot(self):
        print('периметр трапеции ',(self.K+self.L+self.F+self.O))

W1 = ell()
W2 = kv()
W3 = tr()
a = 0
while a!= 4:
    a = int(input ('1 - elleps, 2 - squere, 3- trap: \n'))
    if a == 1:
        W1.ok()
        W1.pk()
    if a == 2:
        W2.oko()
        W2.pko()
    if a == 3:
        W3.pt()
        W3.ot()
