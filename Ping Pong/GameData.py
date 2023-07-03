from turtle import Turtle
import random

BallHEADING_1 = [135, 136, 137, 138, 139, 140,
                 141, 142, 143, 144, 145, 146,
                 147, 148, 149, 150, 151, 152,
                 153, 154, 155, 156, 157, 158,
                 159, 160, 161, 162, 163, 164,
                 165, 166, 167, 168, 169, 170,
                 171, 172, 173, 174, 175, 176,
                 177, 178, 179, 180, 181, 182,
                 183, 184, 185, 186, 187, 188,
                 189, 190, 191, 192, 193, 194,
                 195, 196, 197, 198, 199, 200,
                 201, 202, 203, 204, 205, 206,
                 207, 208, 209, 210, 211, 212,
                 213, 214, 215, 216, 217, 218,
                 219, 220, 221, 222, 223, 224]

BallHEADING_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
                 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
                 315, 316, 317, 318, 319, 320, 321, 322, 323,
                 324, 325, 326, 327, 328, 329, 330, 331, 332,
                 333, 334, 335, 336, 337, 338, 339, 340, 341,
                 342, 343, 344, 345, 346, 347, 348, 349, 350,
                 351, 352, 353, 354, 355, 356, 357, 358, 359]

UP = 90
DOWN = 270
LINE_POSITION = (0, 340)

ALIGNMENT = "center"
FONT = ('Arial', 30, 'bold')

NORTH = 90
EAST = 0
WEST = 180
SOUTH = 270


class Pad(Turtle):
    def __init__(self, pad_position):
        super().__init__()
        self.speed("fastest")
        self.make_pad(pad_position)
        

    def make_pad(self, pad_position):
        self.pu()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.color("white")
        self.goto(pad_position)

    def up(self):
        if 320 > self.ycor() > -320:
            self.setheading(UP)
            self.fd(40)
        else:
            self.bk(15)

    def down(self):
        if 320 > self.ycor() > -320:
            self.setheading(DOWN)
            self.fd(40)
        else:
            self.bk(15)


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.pensize(12)
        self.color("white")
        self.pu()
        self.seth(270)
        self.goto(LINE_POSITION)
        self.net()

    def net(self):
        for x in range(12):
            self.pd()
            self.fd(30)
            self.pu()
            self.fd(30)


class ScoreBoard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.speed("fastest")
        self.score = 0
        self.ht()
        self.color("white")
        self.pu()
        self.goto(pos)
        self.score_display()

    def increase(self):
        self.clear()
        self.score += 1
        self.score_display()

    def score_display(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        print("damn")
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nScore board: {self.score}", align=ALIGNMENT, font=FONT)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=.7, stretch_wid=.7)
        self.shape('circle')
        self.color("white")
        self.winner = 1
        self.pu()
        self.spawn()

    def spawn(self):

        self.goto((0, random.randint(-360, 360)))
        if self.winner == 2:
            self.setheading(random.choice(BallHEADING_2))
        elif self.winner == 1:
            self.setheading(random.choice(BallHEADING_1))

    def move(self):
        self.fd(10)

    def wall_collision(self):
        if EAST < self.heading() < NORTH:
            self.setheading(360 - (NORTH - self.heading()))

        elif NORTH < self.heading() < WEST:
            self.setheading(SOUTH - (WEST - self.heading()))

        elif WEST < self.heading() < SOUTH:
            self.setheading(WEST - (self.heading() - WEST))

        else:
            self.setheading(360 - self.heading())

    def pad_collision(self, heading):
        self.setheading(random.choice(heading))
        self.fd(30)
