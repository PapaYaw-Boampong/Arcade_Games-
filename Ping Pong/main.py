import time
from turtle import Screen
from GameData import Pad, Net, ScoreBoard, Ball,BallHEADING_2,BallHEADING_1

Pad_1_position = (-420, 0)
Pad_2_position = (420, 0)

screen = Screen()
screen.title("Ping Pong ")
screen.setup(width=900, height=750)
screen.bgcolor("black")
screen.tracer(0)

pad_1 = Pad(Pad_1_position)
pad_2 = Pad(Pad_2_position)

net = Net()
score_1 = ScoreBoard((-40, 320))
score_2 = ScoreBoard((40, 320))

ball = Ball()
screen. listen()

screen.onkeypress(fun=pad_2.up, key="Up")
screen.onkeypress(fun=pad_2.down, key="Down")
screen.onkeypress(fun=pad_1.up, key="w")
screen.onkeypress(fun=pad_1.down, key="s")
run = True
while run:
    screen.update()
    ball.move()
    time.sleep(.02)
    if ball.ycor() > 370 or ball.ycor() < -370:
        ball.wall_collision()
    if pad_1.distance(ball) < 25 or (pad_1.distance(ball) < 51 and ball.xcor() < -417):
        ball.pad_collision(BallHEADING_2)
    elif pad_2.distance(ball) < 25 or (pad_2.distance(ball) < 51 and ball.xcor() > 417):
        ball.pad_collision(BallHEADING_1)
    if ball.xcor() > 455:
        ball.spawn()
        score_1.score += 1
        score_1.clear()
        score_1.score_display()
        screen.update()
        ball.winner = 2
    elif ball.xcor() < -455:
        ball.spawn()
        score_2.score += 1
        score_2.clear()
        score_2.score_display()
        screen.update()
        ball.winner = 1
screen.exitonclick()