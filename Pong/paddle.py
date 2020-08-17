import turtle

class Paddle:
    def __init__(self, position):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0) # Speed of animation for turtle module
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup() # so it doesn't draw a line the whole time
        self.paddle.goto(position, 0)

    def move(self, direction):
        y = self.paddle.ycor()
        new_y = y + 20 if direction else y - 20
        self.paddle.sety(new_y)