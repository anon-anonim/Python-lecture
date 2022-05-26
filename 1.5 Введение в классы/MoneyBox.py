#РЕШЕНИЕ
class MoneyBox:
    box = []
    capacity = int()
    status = False
    self = len(box)

    def __init__(self, capacity):
        self.capacity = capacity
                                                   

    def can_add(self, v):
        if v <= self.capacity:
            self.status = True
            return True
        else:
            self.status = False 
            return False                              

    def add(self, v):        
        if self.status == True or self.can_add(v) == True:
            self.box += list('$'*v)
            self.capacity = self.capacity - len(list('$'*v))
            self.status = False 
            return self.capacity