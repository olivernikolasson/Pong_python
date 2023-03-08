import turtle
from turtle import Screen, Turtle
import time
from padel import Padel
from ball import Ball
from score import Score



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Py-Pong - Oliver Nikolasson")
screen.tracer(0)
screen.listen()

r_padel = Padel((350, 0))
l_padel = Padel((-350, 0))

ball = Ball()

screen.onkey(key="Up", fun=r_padel.up)
screen.onkey(key="Down", fun=r_padel.down)
screen.onkey(key="w", fun=l_padel.up)
screen.onkey(key="s", fun=l_padel.down)



score = Score()


game_on = True
while game_on:
    screen.update()
    ball.move()


    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # Collision with padel
    if ball.distance(r_padel) < 50 and ball.xcor() > 340 or ball.distance(l_padel) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        ball.speedinc()

    # out right
    if ball.xcor() > 350:
        ball.out()
        score.l_point()
        ball.speedres()

    # out left
    if ball.xcor() < -350:
        ball.out()
        score.r_point()
        ball.speedres()


screen.exitonclick()

