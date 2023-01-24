from turtle import Turtle, Screen
import time
from random import randint
import Classes
        
Game = Classes

screen = Screen()
screen.title("Snake Game")
screen.setup(Classes.Settings.width + 100, Classes.Settings.height + 200)
screen.tracer(0)

Game.Game.game(screen)

screen.listen()
screen.onkeypress(Classes.Moving.goup, "Up")
screen.onkeypress(Classes.Moving.godown, "Down")
screen.onkeypress(Classes.Moving.goleft, "Left")
screen.onkeypress(Classes.Moving.goright, "Right")

screen.mainloop()
