from turtle import Screen
from data import ScoreBoard, Paddle, Bricks, Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout")
screen.setup(width=1400, height=750)
screen.tracer(0)

#Game components
paddle = Paddle((0, -350))
score_board = ScoreBoard()
ball = Ball()
bricks = Bricks()

#Keys needed to play
screen.listen()
screen.onkey(paddle.right, "Right")
screen.onkey(paddle.left, "Left")

should_cont = True
while should_cont:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #When the ball interacts with the borders.
    if ball.xcor() > 680 or ball.xcor() < -680:
        ball.bounce_x()

    if ball.ycor() > 370:
        ball.bounce_y()

    #When ball-paddle collision is detected.
    if ball.distance(paddle) < 40 and ball.ycor() < -320:
        ball.bounce_y()

    #When a ball-brick collision is detected
    for brick in bricks.bricks:
        if brick.distance(ball) < 40:
            brick.goto(1000, 1000)
            bricks.bricks.remove(brick)
            ball.bounce_y()
            score_board.increase_score()

    #When the ball is detected to leave the field of play
    if ball.ycor() < -450:
        score_board.game_end()
        should_cont = False

screen.exitonclick()
