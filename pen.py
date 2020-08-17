import turtle

class Pen:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("blue")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 250)

    def update_score(self, score_a, score_b):
        self.pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "bold"))