import random
from turtle import Turtle

tracks = [-225, -208, -191, -174,
          -157, -140, -123, -106,
          -89, -72, -55, -38, -21,
          -4, 13, 30, 47, 64, 81,
          98, 115, 132, 149, 166,
          183, 200, 217]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
FONT = ("Courier", 24, "normal")
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []

    def add_cars(self, lvl):
        for i in range(lvl):
            car = Turtle()
            car.seth(180)
            car.shape('square')
            car.pu()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.setpos(400, random.choice(tracks))
            self.car_list.append(car)

    def reset_cars(self, lvl):

        for car in self.car_list:
            car.goto(600, 600)
        self.car_list.clear()
        self.add_cars(lvl)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.LEVEL = 15
        self.game_speed = .07
        self.shape("turtle")
        self.color("white")
        self.pu()
        self.seth(90)
        self.goto(0, -290)

    def move(self):
        self.fd(15)

    def right_turn(self):
        self.goto(self.xcor() + 10, self.ycor())

    def left_turn(self):
        self.goto(self.xcor() - 10, self.ycor())

    def back_turn(self):
        self.bk(15)

    def reset_turtle(self):
        self.LEVEL = 15
        self.color('white')
        self.goto(0, -290)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 3
        self.color("white")
        self.pu()
        self.ht()
        self.level = 1
        self.hs_update()

    def hs_reset(self):
        if self.level > self.highscore:
            with open("highscore.txt", mode='w') as old_data:
                old_data.write(str(self.level))
        self.hs_display()

    def hs_update(self):
        with open("highscore.txt") as old_data:
            self. highscore = int(old_data.readline())
        self.hs_reset()

    def hs_display(self):
        self.goto(220, 280)
        self.write(f"HIGH SCORE : {self.highscore}", align="center", font=('Arial', 15, 'bold'))

    def flag(self, cars, time):
        self.goto(0,0)
        for i in range(3):
            self.write(f"     level {self.level}\nGame on in: \n           {self.count}",
                       align="center",
                       font=('Arial', 30, 'bold'))
            time.sleep(1)
            self.count = self.count - 1
            self.clear()

            for a in range(50):
                car = random.choice(cars.car_list)
                car.fd(random.randint(50, 70))
                self.clear()
        self.hs_update()

    def winner_prompt(self):
        self.goto(0, 0)
        self.write(f"WINNER ;)", align="center", font=('Arial', 30, 'bold'))
