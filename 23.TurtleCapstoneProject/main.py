import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
cars_have_appeared = False
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard = Scoreboard()
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.reset_position()
        car_manager.move_cars()
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT
        scoreboard = Scoreboard()
        scoreboard.increase_level()
        

screen.exitonclick()
