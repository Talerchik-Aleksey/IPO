class line:
    def __init__(self, n):
    	self.line =str(input('Line: ')[:int(n)])
    def find (self):
        print(self.line.count( " "),' - space in line\n' + self.line.lower(),' - new line')

if __name__ == "__main__":
    rect = line(input('Enter size of line: '))
    rect.find()
    # -- / call function -- #
