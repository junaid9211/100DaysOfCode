from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))
        self.shapesize(stretch_wid=1, stretch_len=2)


    def move(self, distance):
        self.backward(distance)



class CarManager:
    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE


    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            self.cars.append(Car())

    def move_cars(self):
        for car in self.cars:
            car.move(self.cars_speed)




    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT


