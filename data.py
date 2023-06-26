from turtle import Turtle
import random

COLOR_LIST = ['royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-620, -370)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 40, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_end(self):
        self.clear()
        self.goto(-120, 0)
        self.pencolor("red")
        self.write(f"Game Over!\nYour Score: {self.score}", font=("Arial", 40, "normal"))


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def right(self, **kwargs):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def left(self, **kwargs):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())


class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.bricks = []

        for row in range(8):
            for column in range(14):
                brick = Turtle()
                brick.speed(0)
                brick.shape("square")
                brick.color(random.choice(COLOR_LIST))
                brick.shapesize(stretch_wid=1.5, stretch_len=4.5)
                brick.penup()
                x = -655 + column * 100
                y = 430 - row * 40
                brick.goto(x, y)
                self.bricks.append(brick)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 1
