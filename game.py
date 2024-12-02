
from ball import  Ball
from paddle import Paddle
import keyboard
import time
from score import  Score
from random import randint

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
PADDLE_WIDTH = 50
PADDLE_HEIGHT = 150
BALL_SPEED = 5
BALL_RADIUS = 5
BALL_COLOR = 'white'



class Game:
    def __init__(self):
        self.running = False
        self.idle = False

    def create_objects(self,ball:Ball,paddle_1:Paddle,paddle_2:Paddle):
        ball = Ball( x=640, y=randint(10, WINDOW_HEIGHT-10), radius=BALL_RADIUS, color=BALL_COLOR,speed=BALL_SPEED)
        if self.idle:
            paddle_1 = Paddle(center_x=75, center_y=WINDOW_HEIGHT // 2, width=PADDLE_WIDTH, height=WINDOW_HEIGHT)
            paddle_2 = Paddle(center_x=1155, center_y=WINDOW_HEIGHT // 2, width=PADDLE_WIDTH, height=WINDOW_HEIGHT)
        else:
            paddle_1 = Paddle(center_x=75, center_y=WINDOW_HEIGHT // 2, width=PADDLE_WIDTH, height=PADDLE_HEIGHT)
            paddle_2 = Paddle(center_x=1155, center_y=WINDOW_HEIGHT // 2, width=PADDLE_WIDTH, height=PADDLE_HEIGHT)


        return [ball,paddle_1,paddle_2]

    def start(self):
        print('Game Started.')
        screen = self.create_objects(Ball, Paddle, Paddle)
        ball = screen[0]
        player_1 = screen[1]
        player_2 = screen[2]
        score = Score()

        self.running = True
        while self.running:
            ball.reflect(0, WINDOW_HEIGHT)
            ball.move()
            ball.hit_paddle(player_1, player_2)
            player_1.handle_controls()
            player_2.handle_controls()
            ball.score_condition(player_1,player_2, score)
            print(ball)

            if keyboard.is_pressed('esc'):
                self.running = False
                self.stop()
                break

    def stop(self):
        self.idle = False
        print('Game stopped.')


    def idle_screen(self):
        self.idle = False
        print('Game Idle Screen')
        screen = self.create_objects(Ball,Paddle,Paddle)
        ball = screen[0]
        player_1 = screen[1]
        player_2 = screen[2]
        score = Score()
        self.running = True
        while self.running:
            time.sleep(0.2)
            ball.reflect(0,WINDOW_HEIGHT)
            ball.move()
            ball.hit_paddle(player_1,player_2)
            player_1.handle_controls()
            player_2.handle_controls()
            ball.score_condition(player_1,player_2, score)

            print(ball)
            print(score)

            if keyboard.is_pressed('esc'):
                break
            elif keyboard.is_pressed('space'):
                self.idle = False
                self.start()
