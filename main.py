from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# Create de scenario
""" instancia de la clase """
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

#Instanciar el objeto serpiente 
snake = Snake()

#Instanciar objeto comida
food = Food()

#Instanciar objeto Score
Scoreboard = Scoreboard()

#Movimientos serpiente
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    

    if snake.head.distance(food) < 15:
        food.refresh()
        Scoreboard.increase_score()
        snake.extend()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        Scoreboard.game_over()

    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            Scoreboard.game_over()


screen.exitonclick()