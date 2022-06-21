from turtle import Turtle, Screen
import random

race_is_on = False
colors_bank = ["red", "green", "black", "yellow", "orange", "purple", "brown", "aqua", "pink"]
turtles = [Turtle(shape="turtle") for i in range(9)]
screen = Screen()
screen.setup(width=500, height=400)
x = -230
y = -180

for i in range(9):
    turtles[i].color(colors_bank[i])
    turtles[i].penup()
    turtles[i].goto(x, y)
    y += 45

player_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")
if player_choice:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            if turtle.pencolor() == player_choice:
                print("Your turtle's won! Congrats!")
            else:
                print("Your turtle's lost!")
            race_is_on = False
            break

screen.exitonclick()
