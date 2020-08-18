import turtle
import time
import functools

import paddle
import ball
import game

Game = game.Game
Paddle = paddle.Paddle
Ball = ball.Ball

game = Game()
paddle_a = Paddle(-350)
paddle_b = Paddle(350)
ball = Ball()

game.window.listen()
game.window.onkeypress(functools.partial(paddle_a.move, True), "w")
game.window.onkeypress(functools.partial(paddle_a.move, False), "s")
game.window.onkeypress(functools.partial(paddle_b.move, True), "Up")
game.window.onkeypress(functools.partial(paddle_b.move, False), "Down")
game.update_score(game.score_a, game.score_b)

while True:
    time.sleep(1/120)
    game.window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

     # Border checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        new_coord = ball.ycor()
        ball.sety(new_coord)
        ball.flip_direction('y')
        game.play_sound("bounce")

    if ball.xcor() > 390 or ball.xcor() < -390:
        point = ball.xcor()
        ball.goto(0, 0)
        ball.flip_direction('x')
        if point > 0:
            game.score_a += 1
        else:
            game.score_b += 1
        game.pen.clear()
        game.update_score(game.score_a, game.score_b)
        game.play_sound("out")

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.flip_direction('x')
        game.play_sound("bounce")


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.flip_direction('x')
        game.play_sound("bounce")
