from tkinter.font import BOLD
from turtle import Turtle, update 

ALIGN = "center"

FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.goto(-200, 270)
        self.color("white")
        self.update_score()
        self.hideturtle()
    
    def update_score(self):
        self.write(f"Score Board: {self.score}", font= FONT, align= ALIGN)

    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER :´( ", font= FONT, align= ALIGN)