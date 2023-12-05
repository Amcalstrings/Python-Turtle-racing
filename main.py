import turtle
from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
screen.listen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make a choice", prompt="which turtle will win the race? select a color from the following: \n"
                                                       "'red' 'orange' 'yellow' 'green' 'blue' 'purple'")
print(user_choice)
turtle.colormode(255)
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-100, -60, -20, 20, 60, 100]

race_on =  False
all_turtles = []
for turtle_index in range(6):
    turtles = Turtle(shape="turtle")
    turtles.penup()
    turtles.color(turtle_colors[turtle_index]) #assign the turtles different colors from the color list
    turtles.goto(x=-240, y=y_pos[turtle_index]) #assign the turtles different positions from the y_pos list
    all_turtles.append(turtles)

if user_choice:
    race_on = True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            race_on = False
            winning_color = turtle.pencolor()
            if user_choice == winning_color:
                print(f"you've won! the {user_choice} color is the winner")
            else:
                print(f"you lost! the {winning_color} color is the winner")

        rand_distance = randint(0,10)
        turtle.forward(rand_distance)















screen.exitonclick()
