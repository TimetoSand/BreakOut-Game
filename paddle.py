from turtle import Turtle

STEP = 20
RIGHT_BORDER = 350
LEFT_BORDER = -RIGHT_BORDER


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("cyan")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.goto(0, -275)
        self.paddle_l = 80

    def reset_screen(self):
        self.goto(0, -275)
        self.shapesize(stretch_wid=1, stretch_len=8)

    def go_left(self):
        edge = self.xcor() - self.paddle_l / 2
        if edge > LEFT_BORDER:
            self.bk(STEP)

    def go_right(self):
        # move paddle right with key press
        edge = self.xcor() + self.paddle_l / 2
        if edge < RIGHT_BORDER:
            self.fd(STEP)

    def mouse_drag(self, x, y):
        # move paddle with mouse click & drag. y cor is constant
        y = -275
        # self.ondrag(None)
        edge_l = LEFT_BORDER + self.paddle_l / 2
        edge_r = RIGHT_BORDER - self.paddle_l / 2
        if x < edge_l:
            self.goto(edge_l, y)
        elif x > edge_r:
            self.goto(edge_r, y)
        else:
            self.goto(x, y)

    def resize(self):
        self.shapesize(stretch_wid=1, stretch_len=12)
        self.goto(0, -275)
