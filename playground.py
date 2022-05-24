from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("BreakOut Game")

leo = Turtle()
leo.shape("square")
leo.color("cyan")
leo.shapesize(stretch_wid=1, stretch_len=8)
leo.penup()
leo.goto(0, -275)

turtles = []
for i in range(8):
    print(i)
    july = Turtle()
    july.shape("square")
    july.color("green")
    july.penup()
    k = i * 20
    july.goto(-70 + k, -255)
screen.exitonclick()