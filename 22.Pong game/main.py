from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s") 

screen.update()
while True:
    screen.update()
    ball.move()
    # Detect collision with top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    # Detect collision with paddles
    if (ball.xcor() > 340 and ball.distance(r_paddle) < 50) or (ball.xcor() < -340 and ball.distance(l_paddle) < 50):
        ball.bounce_x()
    # Detect if ball goes out of bounds
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.reset_position()
        if ball.xcor() > 0:  # Right paddle missed
            l_paddle.goto(-350, 0)  # Reset left paddle
        else:  # Left paddle missed
            r_paddle.goto(350, 0)  # Reset right paddle


# Exit on click
screen.exitonclick()