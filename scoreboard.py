from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 4
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-290, 260)
        self.write(f'Lives: {self.lives}', align='center', font=('Courier', 20, "normal"))
        self.goto(290, 260)
        self.write(f'Score: {self.score}', align='center', font=('Courier', 20, 'normal'))

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def score_points(self, points):
        self.score += points
        self.update_scoreboard()

    def win(self):
        self.home()
        self.write("You win!", align='center', font=('Courier', 60, 'normal'))

    def lose(self):
        self.home()
        self.write("You lose.", align='center', font=('Courier', 60, 'normal'))