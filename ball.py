import turtle

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0) # Speed of animation for turtle module
        self.ball.shape("square")
        self.ball.color("yellow")
        self.ball.penup() # so it doesn't draw a line the whole time
        self.ball.goto(0, 0)
        self.ball.dx = 2 # delta / speed of change
        self.ball.dy = 2 # everytime the ball moves it moves by 1 px 

    def flip_direction(self, direction):
        if direction == 'x':
            self.ball.dx *= -1
        if direction == 'y':
            self.ball.dy *= -1