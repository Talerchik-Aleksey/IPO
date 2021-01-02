class Dete(object):
    def __init__(self, day, mouth, year):
        self.name = name
        self.price = float(price)
        self.maker = maker
    
    def cheack(self):
        self.price= self.price * 0.011
    def cheack_2(self, flag):
        for i in self.name.split():
            if (i == "Samsung") or (i == "samsung"):
                self.price *= 2
        print('name - ' + self.name, '\n' + 'euro price - ', int(self.price),'\u20ac','\n' + 'maker - ', self.maker)    

name = input('name: ')
price = input('price: ')
maker = input('maker: ')

if __name__ == "__main__":
    dete = Dete(name, price, maker)
    dete.cheack_2(dete.cheack())
