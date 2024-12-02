from score import Score
from paddle import Paddle

class Ball:
    def __init__(self, x, y, radius, color,speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.y_speed = speed
        self.x_speed = speed
        self.ghost = False

    #print ball position
    def __str__(self):
        return f'Ball is in {self.x}, {self.y}, speed {self.x_speed}, {self.y_speed}'

    #move the ball
    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed



    #check if ball hit paddle
    def hit_paddle(self,paddle_1: Paddle,paddle_2: Paddle):
        if (self.x <=paddle_1.center_x - paddle_1.width//2):
            if (self.y >=paddle_1.center_y - paddle_1.height//2) and (self.y <= paddle_1.center_y +paddle_1.height//2):
                print('Hit paddle 1')
                self.x_speed = -self.x_speed

        if (self.x >=paddle_2.center_x - paddle_2.width//2):
            if (self.y >=paddle_2.center_y - paddle_2.height//2) and (self.y <= paddle_2.center_y +paddle_2.height//2):
                print('Hit paddle 2')
                self.x_speed = -self.x_speed

    def score_condition(self,paddle_1: Paddle,paddle_2: Paddle,score:Score):
        if self.x <= paddle_1.center_x + paddle_1.width//2:
            if (self.y <= paddle_1.center_y - paddle_1.height//2) or (self.y>=paddle_1.center_y + paddle_1.height//2):
                print('Paddle 1 Miss, Player 2 Scores')
                score.player_2()
                self.reset_ball()
        elif self.x >= paddle_2.center_x - paddle_2.width//2:
            if (self.y <= paddle_2.center_y - paddle_2.height//2) or (self.y>=paddle_2.center_y + paddle_2.height//2):
                print('Paddle 2 Miss, Player 1 Scores')
                score.player_1()
                self.reset_ball()



    def reflect(self,min_y,max_y):
        if self.y >= max_y:
            self.y_speed = -self.y_speed
        elif self.y <= min_y:
            self.y_speed  = -self.y_speed





    def reset_ball(self):
        self.x = 300
        self.y = 300
        self.y_speed = 5
        self.x_speed = 5
        print('Ball reset')
















