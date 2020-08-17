import turtle
import winsound

class Game:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Pong Python by @edwardhorsey")
        self.window.bgcolor("grey")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)
        self.score_a = 0
        self.score_b = 0
    
    def play_sound(self, sound):
        winsound.PlaySound(f"./sounds/{sound}.wav", winsound.SND_ASYNC)
        