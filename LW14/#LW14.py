class Vegetable:

    states = {0: 'none', 1: 'цветет', 2: 'зеленый помидор', 3: 'красный помидор'} # states for save

    def __init__(self, index):
        self._index = index # индекс
        self._state = 0 # стадии states

    def grow(self):
        self._change_state() # метод grow(), который будет переводить овощ на следующую стадию созревания

    def is_ripe(self): # Создайте метод is_ripe(), который будет проверять, что овощ созрел (достиг последней стадии созревания)
        if self._state == 3:
            return True  # for return all
        return False # for return all
    
    def _change_state(self):
        if self._state < 3:
            self._state += 1 # state = 1..2..3
        self._print_state() # Помидор {1} уже states[1, 2, 3]
        
    def _print_state(self):
        print(f'Помидор {self._index} уже {Tomato.states[self._state]}') # Помидор {1} уже states[1, 2, 3]

class Tomato(Vegetable): 

    def __init__(self, index = 1): #fix 02.01.2021
        self._variety = "Агата" #dinamic
        self._state = 0 # стадии states         #fix 02.01.2021
        self._index = index # индекс

    def _give_variety(self):
        print(f'Помидор {self._variety}')
    

class TomatoBush: # куст
    
    variety = "Агата" #static
    
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num)] #fix 02.01.2021
        
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes]) # https://www.w3schools.com/python/ref_func_all.asp#:~:text=The%20all()%20function%20returns,()%20function%20also%20returns%20True.

    def give_away_all(self):
        self.tomatoes = [] #


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник работает...')
        self._plant.grow_all()                  #uhod
        print('Садовник окончил работу')

    def harvest(self):
        print('Садовник собирает урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор урожая окончен')    #take               
        else:
            print('Слишком рано начат собираться урожай. Попробуйте позже.') # all_are_ripe(all([tomato.is_ripe() for tomato in self.tomatoes]))

    def knowledge_base() :
        print('''Harvest time for tomatoes should ideally occur
when the fruit is a mature green and
then allowed to ripen off the vine.
This prevents splitting or bruising
and allows for a measure of control over the ripening process.''') # info

    #--/ end class --#
if __name__ == '__main__':
    Gardener.knowledge_base() # info
    great_tomato_bush = TomatoBush(4) # self.tomatoes
    gardener = Gardener('Сеня', great_tomato_bush)  # self.name,  self._plant
    gardener.work() # 1, 2, 3
    gardener.work() # 1, 2, 3
    gardener.harvest() # print('Слишком рано начат собираться урожай. Попробуйте позже.')
    gardener.work() # 1, 2, 3
    gardener.harvest() # print('Сбор урожая окончен')
    tomato = Tomato()
    tomato._give_variety()
    # print(f'Помидор {TomatoBush.variety}')

    # Next programm with readme !!!!!!!
