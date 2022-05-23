import random
class Bidirectional_dec:
    _adress_space = random.sample(range(0, 40), 10)
    _dec = {x: [None, None, None] for x in _adress_space}
    _first_cell = None
    _last_cell = None
    def _create_new_adress(self):
        for new_adress in range(0, 50):
            if new_adress not in self._adress_space:
                return new_adress
    def __init__(self, list_of_elements):
        for j in self._dec:
            if self._dec[j][0] == None:
                self._current_cell = j
                break
        self._first_cell = self._current_cell
        self._next_cell = None
        self._previous_cell = None
        for elem in list_of_elements:
            for j in self._dec:
                if self._dec[j][0] == None and j != self._current_cell:
                    self._next_cell = j
                    break
            if list_of_elements[len(list_of_elements)-1] == elem:
                self._next_cell = None
                self._last_cell = self._current_cell
            self._dec[self._current_cell] = [elem, self._previous_cell, self._next_cell]
            self._previous_cell = self._current_cell
            self._current_cell = self._next_cell
        

    def convert_to_stack(self):
        return Stack(self.show())

    def insert_at_end(self, element):
        for j in self._dec:
            if self._dec[j][0] == None:
                self._current_cell = j
                break
        self._next_cell = None
        self._dec[self._current_cell] = [element, self._previous_cell, self._next_cell]
        self._dec[self._previous_cell][2] = self._current_cell
        self._next_cell = None
        self._previous_cell = self._current_cell
        self._last_cell = self._current_cell

    def remove_at_end(self):
        temp = self._previous_cell
        self._previous_cell = self._dec[self._previous_cell][1]
        self._dec[temp] = [None, None, None]
        self._dec[self._previous_cell][2] = None
        self._last_cell = self._previous_cell

    def insert_at_start(self, element):
        for j in self._dec:
            if self._dec[j]==[None,None,None]:
                self._dec[self._first_cell][1] = j
                self._dec[j] = [element, None, self._first_cell]
                self._first_cell = j
                break
    def remove_at_start(self):
        temp = self._first_cell
        self._first_cell = self._dec[self._first_cell][2]
        self._dec[self._first_cell][1] = None
        self._dec[temp] = [None, None, None]

    def show(self):
        temp = self._first_cell
        list_of_elements = []
        while True:
            list_of_elements.append(self._dec[temp][0])
            temp = self._dec[temp][2]
            if temp == None:
                break
        return list_of_elements

    def find(self):
        pass

class Stack:
    _adress_space = random.sample(range(0, 40), 10)
    _stack= {x: [None, None, None] for x in _adress_space}
    _first_cell = None
    _last_cell = None

    def __init__(self, list_of_elements):
        for j in self._stack:
            if self._stack[j][0] == None:
                self._current_cell = j
                break
        self._first_cell = self._current_cell
        self._next_cell = None
        self._previous_cell = None
        for elem in list_of_elements:
            for j in self._stack:
                if self._stack[j][0] == None and j != self._current_cell:
                    self._next_cell = j
                    break
            if list_of_elements[len(list_of_elements)-1] == elem:
                self._next_cell = None
                self._last_cell = self._current_cell
            self._stack[self._current_cell] = [elem, self._previous_cell, self._next_cell]
            self._previous_cell = self._current_cell
            self._current_cell = self._next_cell

    def insert_at_end(self, element):
        for j in self._stack:
            if self._stack[j][0] == None:
                self._current_cell = j
                break
        self._next_cell = None
        self._stack[self._current_cell] = [element, self._previous_cell, self._next_cell]
        self._stack[self._previous_cell][2] = self._current_cell
        self._next_cell = None
        self._previous_cell = self._current_cell
        self._last_cell = self._current_cell

    def remove_at_end(self):
        temp = self._previous_cell
        self._previous_cell = self._stack[self._previous_cell][1]
        self._stack[temp] = [None, None, None]
        self._stack[self._previous_cell][2] = None
        self._last_cell = self._previous_cell

    def show(self):
        temp = self._first_cell
        list_of_elements = []
        while True:
            list_of_elements.append(self._stack[temp][0])
            temp = self._stack[temp][2]
            if temp == None:
                break
        return list_of_elements

if __name__ == "__main__":
    dec = Bidirectional_dec(input().split())
    #stack = dec.convert_to_stack()
    #print(stack.show())
    #print(stack._stack)
    #print("_first_cell",dec._first_cell)
    #print("_last_cell",dec._last_cell)
    
    dec.insert_at_start(input("insert_at_start"))
    print(dec._dec)
    #print("_first_cell",dec._first_cell)
    #print("_last_cell",dec._last_cell)
    #print(dec.show())
    #dec.remove_at_end()
    #print(dec._dec)    
    #print("_first_cell",dec._first_cell)
    #print("_last_cell",dec._last_cell)