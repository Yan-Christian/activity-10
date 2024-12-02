

class Score:
    def __init__(self):
        self.color = 'white'
        self.player_1_points = 0
        self.player_2_points = 0
        self.max_score = 5

    def __str__(self):
        return (f'Player 1: {self.player_1_points} \n'
                f'Player 2: {self.player_2_points}')


    def player_1(self):
        self.player_1_points += 1

    def player_2(self):
        self.player_2_points += 1










