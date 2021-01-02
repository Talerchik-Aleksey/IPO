import random
# -- / randomint -- #
from datetime import date
from datetime import time
from datetime import datetime
# -- / datetime.now() -- #
class house:
    def __init__(self):
        self.number = datetime.now()
        self.large = int(input('Enter size: '))
        self.floors = int(input('Enter floors: '))
        self.flats = int(input('Enter flats: '))
        self.entrance = int(input('Enter entrance: '))
        # -- / enter information -- #
    def find(self):
       print('house №',self.number,'-->')  
       print(self.large/self.floors, ' - size floor')
       print(self.flats/self.entrance, ' - size flats in entrance')
       print((self.flats/self.entrance)/self.floors, ' - flats in floors')
       # -- / output -- #
if __name__ == "__main__":
    house_in = house()
    house_in.find()
    # -- / call function -- #
