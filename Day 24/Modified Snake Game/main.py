import turtle
from turtle import Screen
import time
import random
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from colors import color_palettes


COLOR_PALETTE = random.choice(color_palettes)
BG_COLOR = COLOR_PALETTE['bgcolor']
SNAKE_COLOR = COLOR_PALETTE['snakecolor']
FOOD_COLOR = COLOR_PALETTE['foodcolor']

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

RIGHT_BOUNDARY = WINDOW_WIDTH // 2 - 20
LEFT_BOUNDARY = -1 * (WINDOW_WIDTH // 2)
TOP_BOUNDARY = WINDOW_HEIGHT // 2
BOTTOM_BOUNDARY = -1 * (WINDOW_HEIGHT // 2) + 10

refresh_rate = 0.13
level_counter = 0


turtle.colormode(255)
screen = Screen()
screen.bgcolor(BG_COLOR)
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.title('My Snake Game')
screen.tracer(0)


snake = Snake(SNAKE_COLOR)
food = Food(color=FOOD_COLOR, xlim=(LEFT_BOUNDARY+30, RIGHT_BOUNDARY-30), ylim=(BOTTOM_BOUNDARY+30, TOP_BOUNDARY-50))
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(key='Up', fun=snake.up)
screen.onkeypress(key='Down', fun=snake.down)
screen.onkeypress(key='Left', fun=snake.left)
screen.onkeypress(key='Right', fun=snake.right)

screen.onkeypress(key='w', fun=snake.up)
screen.onkeypress(key='s', fun=snake.down)
screen.onkeypress(key='a', fun=snake.left)
screen.onkeypress(key='d', fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(refresh_rate)


    # Detect collision with the food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        level_counter += 1

        if level_counter >= 5:
            if refresh_rate > 0.6:
                refresh_rate -= 0.01

            level_counter = 0
            scoreboard.current_level += 1

        scoreboard.increase_score()



    # Detect collision with the wall
    x_position = snake.head.xcor()
    y_position = snake.head.ycor()
    if x_position > RIGHT_BOUNDARY or x_position < LEFT_BOUNDARY or y_position > TOP_BOUNDARY or y_position < BOTTOM_BOUNDARY:
        refresh_rate = 0.13
        level_counter = 0
        scoreboard.reset()
        snake.reset()

    # Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            refresh_rate = 0.13
            level_counter = 0
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

