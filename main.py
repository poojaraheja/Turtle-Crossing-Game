import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
car_manager = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

for i in range(8):
    car_manager.new_car()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.new_car()
    car_manager.car_move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20 :
            game_is_on = False
            score.print()
    if player.is_at_finish_line():
        score.increase()
        player.go_to_start()
        car_manager.level_up()

screen.exitonclick()
