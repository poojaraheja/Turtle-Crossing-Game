from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.all_cars = []
        self.spee = STARTING_MOVE_DISTANCE
    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            pooja = Turtle("square")
            pooja.penup()
            pooja.shapesize(stretch_wid=1, stretch_len=3)
            pooja.pooja = random.choice(COLORS)
            pooja.color(pooja.pooja)
            new_y = random.randint(-250, 250)
            pooja.goto(280, new_y)
            self.all_cars.append(pooja)
    def car_move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.spee += MOVE_INCREMENT