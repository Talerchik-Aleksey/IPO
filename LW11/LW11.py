class Date(object):
    def __init__(self, day, mouth, year):
        self.day = int(day)
        self.mouth = int(mouth)
        self.year = int(year)
        self.flag = False
    def cheack(self):
        if (self.day == self.mouth) and ( self.mouth < 12):
            self.flag = True
    def cheack_2(self, flag):
        if self.flag == True:
            print(self.day, int(self.mouth) + 1, self.year)

day = input('day: ')
mouth = input('mouth: ')
year = input('year: ')

if __name__ == "__main__":
    dete = Date(day, mouth, year)
    dete.cheack_2(dete.cheack())
