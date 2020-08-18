import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0) # Speed of animation for turtle module
        self.shape("square")
        self.color("yellow")
        self.penup() # so it doesn't draw a line the whole time
        self.goto(0, 0)
        self.dx = 2 # delta / speed of change
        self.dy = 2 # everytime the ball moves it moves by 1 px 

    def flip_direction(self, direction):
        if direction == 'x':
            self.dx *= -1
        if direction == 'y':
            self.dy *= -1