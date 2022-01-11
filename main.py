from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

end = False
delay_on_ball = 0.1

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))

ball = Ball()

r_score = Score((110, 190))
l_score = Score((-110, 190))


screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)

while end == False:
    time.sleep(delay_on_ball)
    screen.update()

    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    if ball.distance(r_paddle) <= 50 and ball.xcor() >= 340:
        delay_on_ball *= 0.8
        ball.reflect_left()

    if ball.distance(l_paddle) <= 50 and ball.xcor() <= -340:
        delay_on_ball *= 0.8
        ball.reflect_right()

    if ball.xcor() > 390:
        delay_on_ball = 0.1
        ball.goto(0, 0)
        ball.reflect_left()
        l_score.add_to_score()

    if ball.xcor() < -390:
        delay_on_ball = 0.1
        ball.goto(0, 0)
        ball.reflect_right()
        r_score.add_to_score()


screen.mainloop()
