from turtle import Turtle


class Brick(Turtle):

    def __init__(self, position, color, value):
        super().__init__("square")
        self.value = value
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)

    def get_value(self):
        return self.value

    def destroy(self):
        self.goto(900, 900)
