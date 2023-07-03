from turtle import Turtle
import random
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
snake_pos = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 22
Food_list = []
'''
FOOD POSITION GENERATOR
MOVE_DISTANCE required 
xps=[]
yps=[]

for px in range(-320, 320, 20):  
    xps.append(px)          
for py in range(-320, 320, 20):
    yps.append(px)

'''


class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for i in snake_pos:
            self.grow(i)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_seg_pos_x = self.segments[seg_num - 1].xcor()
            new_seg_pos_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_seg_pos_x, new_seg_pos_y)
        self.segments[0].fd(MOVE_DISTANCE)

    def grow(self, pos):
        segment = Turtle()
        segment.pu()
        segment.shape("square")
        segment.color("white")
        segment.goto(pos)
        self.segments.append(segment)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def bitten(self):
        for i in self.segments:
            i.color('red')

    def reset(self):
        for i in self.segments:
            i.goto(350,350)
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("green")
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(stretch_len=.5, stretch_wid=.5)

    def make_food(self):
        xps = random.randint(-280, 280)
        yps = random.randint(-279, 280)
        self.goto(xps, yps)


ALIGNMENT = "center"
FONT = ('Arial', 15, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as h_value:
            self.high_score = int(h_value.read())
        self.score = 0
        self.ht()
        self.color("white")
        self.pu()
        self.goto(0, 230)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score board: {self.score}  High Score: {self.high_score}",align=ALIGNMENT, font=FONT )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../OneDrive/Desktop/data.txt", mode="w") as h_value:
                h_value.write(f"{self.score}")
        self.score = 0
        self.update()
