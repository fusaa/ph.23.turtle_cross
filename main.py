import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

player = Player()
carmanager = []
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move,"Up")

cycle = 0
step = 0
carmanager.append(CarManager())
# lele = CarManager()
while game_is_on:
    if cycle == 0:
        carmanager.append(CarManager())
        carmanager[-1].step = step
        for a in range(len(carmanager)):
            carmanager[a].step = step

    cycle += 1

    if cycle == 5:
        cycle = 0

    # Detects colision:
    for a in range(len(carmanager)):
        carmanager[a].move()
        if player.distance(carmanager[a]) < 20:
            print(f"hit {a}")
            scoreboard.game_over()
            game_is_on = False

    # Detects Score and go next level
    if player.ycor() > 270:
        print("top")
        player.goto(0, -280)
        scoreboard.update_score()
        step += 10

    time.sleep(0.1)
    screen.update()


screen.exitonclick()
