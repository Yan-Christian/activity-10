

class Block:
    def __init__(self,x,y,color):
        self.width = 20
        self.height = 10
        self.x = x
        self.y = y
        self.height = 10
        self.color = color

    def __str__(self):
        return f'{self.color} block at {self.x,self.y}'













