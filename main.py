import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(tim.move_forward, "Up")
screen.onkey(tim.move_back, "Down")
screen.onkey(tim.move_forward, "w")
screen.onkey(tim.move_back, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            scoreboard.game_over()
            game_is_on = False

    if tim.ycor() > 300:
        tim.goto(0, -280)
        car_manager.next_level()
        scoreboard.add_point()
        scoreboard.update_scoreboard()




screen.exitonclick()
