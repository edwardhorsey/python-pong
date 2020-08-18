import turtle

class Paddle(turtle.Turtle):
    def __init__(self, position):
        turtle.Turtle.__init__(self)
        self.speed(0) # Speed of animation for turtle module
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup() # so it doesn't draw a line the whole time
        self.goto(position, 0)

    def move(self, direction):
        y = self.ycor()
        new_y = y + 20 if direction else y - 20
        self.sety(new_y)