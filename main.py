from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# screen is the object of Screen() class, which is imported from turtle
screen = Screen()

# the size of the game screen is 600 by 600
screen.setup(width=600, height=600)

# the background color of screen
screen.bgcolor("black")

# the title of the game
screen.title("The Snake Game")

# tracer function is used to turn turtle animation on or off and set a delay for update drawings.
screen.tracer(0)    #when we use screen.tracer(0) the snkae is disappare bcoz tracer turn off the animation

snake= Snake()

food = Food()

scoreboard = Scoreboard()
# NOW we call listen() method to statr listing key strocks
screen.listen()
# now we create a key to move
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# move snake_____________________________________________________________________

# code to move the snake forword
game_is_on = True
while game_is_on:
    screen.update() #tracer hide the animations of the snake,
    # so we update the screen after every stap to view the activity of the snake
    time.sleep(.1) #the updater screen is visiable for the .1s of time
    snake.move()

    # now when snake eat the food the food need to disappare from its present place and need to appare at different place

    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #detcet collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False
        scoreboard.game_over()

    #detect collisio with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False

            scoreboard.game_over()
            #when we run this code in if condition the game is over at start,
            # bcz the distance of the head of the snake is not more the the 10px so we need to bypass that
            #so we use the above code
# __________________________________________________________________________________

# screen is invisiable when we click on the screen
screen.exitonclick()