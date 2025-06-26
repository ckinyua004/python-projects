import turtle
import pandas

screen = turtle.Screen()
screen.title("USA STATES GAME")

image = "./25.CSV/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./25.CSV/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'Guess the State.{len(guessed_states)}/51' ,prompt='Add another state').title()
    print(answer_state)

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

# def get_mouse_coor(x, y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_coor)
# turtle.mainloop()

screen.exitonclick( )

