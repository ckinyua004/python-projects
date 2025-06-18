from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False

screen.setup(width= 500, height= 400)
user_bet = screen.textinput(title="Make your input", prompt="Which turtle will win the race: Enter a color: ")

colors = ["red" ,"orange", "yellow", "green", "blue", "purple", "black"]
y_positions = [1, -30, 30, -60, 60, -90, 90]
all_turtles = []

if user_bet:
    is_race_on = True

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()