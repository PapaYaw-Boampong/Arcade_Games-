import random
import time
from turtle import Screen
from GameData import Player, CarManager, Scoreboard


screen = Screen()
screen.setup(width=640, height=620)
screen.title("Turtle crossing game ")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
cars = CarManager()


def game(lvl):
    run = True
    global player
    screen.onkeypress(key="Up", fun=player.move)
    screen.onkeypress(key="Down", fun=player.back_turn)
    screen.onkeypress(key="Left", fun=player.left_turn)
    screen.onkeypress(key="Right", fun=player.right_turn)
    screen.tracer(0)

    cars.add_cars(lvl)
    scoreboard.flag(cars,time)

    while run:
        screen.update()
        time.sleep(player.game_speed)
        car = random.choice(cars.car_list)
        car.fd(random.randint(25, 40))
        for car in cars.car_list:
            if car.xcor() < -280:
                car.setpos(280, random.randint(-280, 280))
            if player.distance(car) < 25.3:
                player.color('red')
                scoreboard.goto(0,0)
                scoreboard.write(f"OUCH  !!! ", align="center", font=('Arial', 30, 'bold'))
                screen.update()
                time.sleep(1)
                scoreboard.clear()
                scoreboard.hs_update()
                player.reset_turtle()
                cars.reset_cars(player.LEVEL)
                scoreboard.count = 3
                screen.update()
                scoreboard.flag(cars,time)

        if player.ycor() > 280:
            scoreboard.level += 1
            scoreboard.winner_prompt()
            time.sleep(1)
            scoreboard.clear()
            cars.reset_cars(player.LEVEL)
            player.reset_turtle()
            screen.update()
            time.sleep(1)
            scoreboard.count = 3
            cars.car_list.clear()
            if player.game_speed < 0:
                print("Game completed,..... Ahh why :/")
            else:
                player.game_speed -= 0.009
            scoreboard.hs_update()
            player.reset_turtle()
            cars.reset_cars(player.LEVEL)
            screen.update()
            scoreboard.flag(cars, time)
            cars.add_cars(player.LEVEL+1)



    screen.exitonclick()


game(player.LEVEL)