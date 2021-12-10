from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]#we togle the head of the smake
        self.head.color("red")
    # create snake__________________________________________________________________

    # creating 3 turtle with shape of square and
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)




    # when the snake eat the food the size of snake need to be increased by 1 so___

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        # appending the segment list
        self.segments.append(new_segment)
    def extend(self):
        #add a new segment to the snake.

        self.add_segment(self.segments[-1].position())  #segments[-1] mean the 3rd segment of the snake

# _________________________________________________________________________________





    # move Snake_____________________________________________________________________
    def move(self):
        # our snake's segment are not linked to gather mean when we say turn left then the first
        # squire is move left but the other are move forword so now we do 1 thing that is
        # first we move 3re square to the position of the 2nd square and the move 2nd to the
        # place of first then at last move 1st squire to forword or left or right so we using for loop

        # in for loop it start with last square which is len(segment)-1 (3rd square) and stop al
        # 0th square
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # now we hold the last segment from the our list of segments.using goto we set it to to the particular x and y position
            # and we passing the cordinate of x and y to the goto of
            self.segments[seg_num].goto(new_x, new_y)
        # now all don but all 3 square are combine together,so to solve this problerm we need to move first segment to forword
        self.head.forward(MOVE_DISTANCE)


# ___________________________________________________________________________________


#change diraction___________________________________________________________________


    def up(self):
        # our snake move backward also, to fix this we use if condition
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




