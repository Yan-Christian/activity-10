from walls import Walls
import keyboard

class Paddle:
    def __init__(self,center_x,center_y,width,height):
        self.width = width
        self.height = height
        self.center_x = center_x
        self.center_y = center_y
        self.color = 'Blue'

    def __str__(self):
        return f'Paddle is in {self.center_x - self.width//2} to {self.center_x + self.width//2}'

    def check_max_min(self,left_wall:Walls,right_wall:Walls):
        if self.center_x - self.width//2 <=  left_wall.x + left_wall.width:
            self.center_x = left_wall.x + left_wall.width
        elif self.center_x + self.width//2 >= right_wall.x + right_wall.width:
            self.center_x = right_wall.x + right_wall.width

    def handle_controls(self):

        if keyboard.is_pressed('left'):
            self.center_x = self.center_x - 5
            print(f'Paddle moved to {self.center_x}')
        elif keyboard.is_pressed('right'):
            self.center_x = self.center_x + 5
            print(f'Paddle moved to {self.center_x}')






