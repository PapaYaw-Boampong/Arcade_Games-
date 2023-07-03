import time
from GameData import Snake, Food, ScoreBoard
from turtle import Screen

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game ")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

snake.make_snake()
screen.listen()

screen.onkey(fun=snake.move_right, key="Right")

screen.onkey(fun=snake.down, key="Down")

screen.onkey(fun=snake.up, key="Up")

screen.onkey(fun=snake.move_left, key="Left")
run = True

while run:
    screen.update()
    time.sleep(.12)
    snake.move()
    for x in snake.segments[1:]:
        if snake.head.distance(x) < 17:
            snake.bitten()
            score_board.reset()
            snake.reset()
            screen.update()
    if snake.head.distance(food) < 15:
        score_board.score += 1
        score_board.update()
        food.make_food()
        snake.grow(snake.segments[-1].pos())
    if (snake.head.xcor() < -280 or snake.head.xcor() > 280) or (snake.head.ycor() < -280 or snake.head.ycor() > 280):
        snake.bitten()
        screen.update()
        time.sleep(.5)
        score_board.reset()
        snake.reset()
        screen.update()
screen.exitonclick()


