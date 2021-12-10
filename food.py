from turtle import Turtle
import random


# Food class inherit from Turtle class

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # normally the size of turtle(circle) is 20 by 20 but we chang it in next line in the half size
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()



    # now we want the turtle is visible at the random place but not at the edge of the frame that's why
    def refresh(self):
        random_x = random.randint(-270,270)
        random_y = random.randint(-270,270)
        self.goto(random_x,random_y)
