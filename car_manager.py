from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = STARTING_MOVE_DISTANCE * 0.50


class CarManager:
    def __init__(self, level):
        self.car = Turtle('square')
        self.car.shapesize(stretch_wid=1, stretch_len=2)
        self.car.penup()
        self.car.color(random.choice(COLORS))
        # to generate a random starting location of each Car
        STARTING_LOCATION = (300, random.randint(-250, 250))
        self.car.goto(STARTING_LOCATION)
        self.check = False  # to destroy the car when it reaches the end
        self.location = self.car.xcor()
        self.level = level

    def move(self):

        if self.check == False:
            # Calculating the speed of the car
            self.car.setx(self.car.xcor() -
                          STARTING_MOVE_DISTANCE - self.level*MOVE_INCREMENT)

        if self.car.xcor() <= -300:
            # removing the turtle
            self.check = True
            self.car.hideturtle()

    def speedup(self):

        global STARTING_MOVE_DISTANCE
        # Increasing the speed of the car after  every lvl
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
