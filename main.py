from turtle import Turtle, Screen
from pad import Pad
from ball import Ball
import time
from score import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


pad1 = Pad((350, 0))
pad2 = Pad((-350, 0))
ball = Ball((0, 0))
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(pad1.go_up, "Up")
screen.onkey(pad1.go_down, "Down")

screen.onkey(pad2.go_up, "w")
screen.onkey(pad2.go_down, "a")


hello_kitty = True
while hello_kitty:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(pad1) < 50 and ball.xcor() > 320 or ball.distance(pad2) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # pad 1
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.pad_2_point()

    # pad 2
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.pad_1_point()






screen.exitonclick()