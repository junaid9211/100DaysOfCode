import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

COLOR_PALETTE = {
        'bgcolor': (24, 24, 24),
        'paddlecolor': (135, 88, 255),
        'ballcolor': (92, 184, 228)
    }

BGCOLOR = COLOR_PALETTE['bgcolor']
PADDLE_COLOR = COLOR_PALETTE['paddlecolor']
BALL_COLOR = COLOR_PALETTE['ballcolor']

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

turtle.colormode(255)
screen = Screen()
screen.bgcolor(BGCOLOR)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle(color=PADDLE_COLOR, position=(350, 0))
l_paddle = Paddle(color=PADDLE_COLOR, position=(-350, 0))
ball = Ball(color=BALL_COLOR)
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key='Up', fun=r_paddle.up)
screen.onkeypress(key='Down', fun=r_paddle.down)
screen.onkeypress(key='w', fun=l_paddle.up)
screen.onkeypress(key='s', fun=l_paddle.down)

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r_paddle or l_paddle
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 60) or (ball.xcor() < -320 and ball.distance(l_paddle) < 60):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()
