

class Score:
    def __init__(self):
        self.color = 'white'
        self.points = 0
        self.max_score = 448

    def __str__(self):
        return f'Actual Score: {self.points}'


    def update_score(self, color):
        if color == 'yellow':
            self.points += 1
        elif color == 'green':
            self.points +=3
        elif color == 'orange':
            self.points +=5
        elif color == 'red':
            self.points +=7
        else:
            self.points +=0
        return True




