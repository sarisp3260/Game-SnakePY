from turtle import Turtle

import random


colors = ["blue","orange","pink","brown","purple"]

#lo que esta dentro de los parentesis son la herencia de la clase Turtle en la cual herada todos los metodos
class Food(Turtle): 
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(colors))
        self.refresh()

    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
