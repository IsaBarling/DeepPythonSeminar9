import turtle

class PingPongGame:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Ping Pong Game")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

        self.paddle_a = PaddleMain(-350, 0)
        self.paddle_b = PaddleMain(350, 0)
        self.ball = BallMain()

        self.window.listen()
        self.window.onkeypress(self.paddle_a.move_up, "w")
        self.window.onkeypress(self.paddle_a.move_down, "s")
        self.window.onkeypress(self.paddle_b.move_up, "Up")
        self.window.onkeypress(self.paddle_b.move_down, "Down")

        self.is_game_over = False

    def play(self):
        while not self.is_game_over:
            self.window.update()
            self.ball.move()

            # Обработка столкновения мяча с ракетками
            if self.ball.is_collision_paddle(self.paddle_a) or self.ball.is_collision_paddle(self.paddle_b):
                self.ball.bounce()

            # Обработка столкновения мяча с границами поля
            if self.ball.is_collision_wall():
                self.ball.bounce_wall()

            # Проверка, желает ли игрок продолжить или завершить игру
            choice = input("Желаете продолжить игру? (y/n): ")
            if choice.lower() == "n":
                self.is_game_over = True

        self.window.mainloop()

class PaddleMain:
    def __init__(self, x, y):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=6, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, y)

    def move_up(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def move_down(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)

class BallMain:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(1)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.dx = 2
        self.dy = 2

    def move(self):
        x = self.ball.xcor()
        y = self.ball.ycor()
        x += self.dx
        y += self.dy
        self.ball.setx(x)
        self.ball.sety(y)

    def bounce(self):
        self.dx *= -1

    def bounce_wall(self):
        self.dy *= -1

    def is_collision_paddle(self, paddle):
        if (self.dx > 0 and paddle.paddle.xcor() - 20 < self.ball.xcor() < paddle.paddle.xcor() + 20) or \
           (self.dx < 0 and paddle.paddle.xcor() - 20 < self.ball.xcor() < paddle.paddle.xcor() + 20):
            if paddle.paddle.ycor() - 50 < self.ball.ycor() < paddle.paddle.ycor() + 50:
                return True
        return False

    def is_collision_wall(self):
        y = self.ball.ycor()
        return y > 290 or y < -290

game = PingPongGame()
game.play()
