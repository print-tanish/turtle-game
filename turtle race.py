from turtle import Turtle, Screen
import random
is_race_on=False
all_turtles=[]
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="which color tutrle will win the race??")
y_axis=[-160,-80,0,80,160]
colors=["red","orange","yellow","green","blue"]
for turtle_index in range(0,5):
  
 tim=Turtle(shape="turtle")
 tim.color(colors[turtle_index])
 tim.penup()
 tim.goto(x=-230,y=y_axis[turtle_index])
 all_turtles.append(tim)


if user_bet:
   is_race_on=True
while is_race_on:
   for turtle in all_turtles:
    if turtle.xcor()>230:
      is_race_on=False
      winning_color=turtle.pencolor()
      if winning_color==user_bet:
        print(f"You have won, {winning_color} turtle is the winner")
      else:
        print(f"You lose,{winning_color} turtle is the winner")
    turtle.forward(random.randint(0,10))  



screen.exitonclick()

