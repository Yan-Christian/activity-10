import keyboard

class Paddle:
    def __init__(self,center_x,center_y,width,height):
        self.width = width
        self.height = height
        self.center_x = center_x
        self.center_y = center_y
        self.color = 'Blue'

    def __str__(self):
        return f'Paddle is in {self.center_x} {self.center_y - self.height//2} to {self.center_y + self.height//2}'

    def handle_controls(self):

        if keyboard.is_pressed('w'):
            self.center_y = self.center_y - 5
            print(f'Player 1 moved to {self.center_y}')
        elif keyboard.is_pressed('s'):
            self.center_y = self.center_y + 5
            print(f'Player 1 moved to {self.center_y}')
        elif keyboard.is_pressed('8'):
            self.center_y = self.center_y - 5
            print(f'Player 2 moved to {self.center_y}')
        elif keyboard.is_pressed('5'):
            self.center_y = self.center_y + 5
            print(f'Player 2 moved to {self.center_y}')










