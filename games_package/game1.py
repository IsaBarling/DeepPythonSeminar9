import turtle
import random

class SnakeGame:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Snake Game")
        self.window.bgcolor("black")
        self.window.setup(width=600, height=600)
        self.window.tracer(0)

        self.snake = Snake()
        self.food = Food()

        self.window.listen()
        self.window.onkey(self.snake.turn_left, "Left")
        self.window.onkey(self.snake.turn_right, "Right")
        self.window.onkey(self.snake.turn_up, "Up")
        self.window.onkey(self.snake.turn_down, "Down")

        self.is_game_over = False

    def play(self):
        while not self.is_game_over:
            self.window.update()
            self.snake.move()

            if self.snake.is_collision(self.food):
                self.snake.grow()
                self.food.move()

            if self.snake.is_collision_wall() or self.snake.is_collision_self():
                self.is_game_over = True

        self.window.mainloop()

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            segment = turtle.Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        self.segments[0].forward(20)

    def turn_left(self):
        self.segments[0].setheading(180)

    def turn_right(self):
        self.segments[0].setheading(0)

    def turn_up(self):
        self.segments[0].setheading(90)

    def turn_down(self):
        self.segments[0].setheading(270)

    def grow(self):
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        self.segments.append(segment)

    def is_collision(self, other):
        return self.segments[0].distance(other.food) < 20

    def is_collision_wall(self):
        x = self.segments[0].xcor()
        y = self.segments[0].ycor()
        return abs(x) > 290 or abs(y) > 290

    def is_collision_self(self):
        for segment in self.segments[1:]:
            if self.segments[0].distance(segment) < 20:
                return True
        return False

class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.move()

    def move(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.food.goto(x, y)

game = SnakeGame()
game.play()
