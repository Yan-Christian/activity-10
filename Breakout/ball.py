from blocks import Block
from walls import Walls
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

    #check if ball hits walls
    def hit_wall(self,left_wall: Walls, right_wall: Walls,upper_wall: Walls,ghost):
        if self.x <= left_wall.x:
            self.x_speed = -self.x_speed
            self.x = left_wall.x + self.radius
            print('Hit left Wall')
        elif self.x >= right_wall.x:
            self.x_speed = -self.x_speed
            self.x = right_wall.x - self.radius
            print('Hit right Wall')
        elif self.y <= upper_wall.y:
            self.y_speed = -self.y_speed
            self.y = upper_wall.y + self.radius
            print('Hit upper Wall')

        if ghost:
            self.toggle_ghost()

    #check if ball hit paddle
    def hit_paddle(self,paddle: Paddle,ghost):
        if self.x <= (paddle.center_x - paddle.width//2) and self.y >= (paddle.center_y):
            print('Hit paddle!')
            self.set_speed('paddle',self.x_speed)
            self.y = paddle.center_y - paddle.height//2 - self.radius
            if ghost:
                self.toggle_ghost()
        elif self.x >= (paddle.width//2 - paddle.center_x) and self.y >= paddle.center_y:
            print('Hit paddle!')
            self.set_speed('paddle',self.x_speed)
            self.y = paddle.center_y - paddle.height//2 - self.radius
            if ghost:
                self.toggle_ghost()
        elif self.y >= paddle.center_y:
            print('Paddle Miss')
            self.reset_ball()

    def hit_block(self,block:Block):
        if (self.x <= block.x - block.width//2) or (self.x >= block.x + block.width//2):
            if (self.y <= block.y) and (self.y <= block.y + block.height):
                print(f'Hit {block.color} block')

                return True
            else:
                return False


    def set_speed(self,color,x_speed):
        if color == 'yellow':
            self.y_speed = 6
            if x_speed > 0:
                self.x_speed = 6
            else:
                self.x_speed = -6
        elif color == 'green':
            self.y_speed = 6.5
            if x_speed > 0:
                self.x_speed = 6.5
            else:
                self.x_speed = -6.5

        elif color == 'orange':
            self.y_speed = 7
            if x_speed > 0:
                self.x_speed = 7
            else:
                self.x_speed = -7

        elif color == 'red':
            self.y_speed = 7.5
            if x_speed > 0:
                self.x_speed = 7.5
            else:
                self.x_speed = -7.5

        else:
            self.y_speed = -6
            if x_speed > 0:
                self.x_speed = 6
            else:
                self.x_speed = -6


    def reset_ball(self):
        self.x = 300
        self.y = 300
        self.y_speed = 6
        self.x_speed = 6
        print('Ball reset')

    def toggle_ghost(self):
        self.ghost = not self.ghost
        print(f'Ball is ghost = {self.ghost} ')















