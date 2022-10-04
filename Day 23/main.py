import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

player = Player()
# car = Car()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(key='w', fun=player.up)
screen.onkeypress(key='s', fun=player.down)
screen.onkeypress(key='Up', fun=player.up)
screen.onkeypress(key='Down', fun=player.down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()

    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        scoreboard.update_level()
        car_manager.increase_speed()




screen.exitonclick()
