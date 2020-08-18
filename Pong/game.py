import turtle
import winsound

class Game():
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Pong Python by @edwardhorsey")
        self.window.bgcolor("grey")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("blue")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 250)
        self.score_a = 0
        self.score_b = 0

    def update_score(self, score_a, score_b):
        self.pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "bold"))
    
    def play_sound(self, sound):
        winsound.PlaySound(f"./Pong/sounds/{sound}.wav", winsound.SND_ASYNC)