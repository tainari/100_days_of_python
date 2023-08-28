from turtle import Turtle

class Net:
    def __init__(self,window_height = 500):
        t = Turtle()
        t.hideturtle()
        t.pencolor("white")
        t.pensize(5)
        t.up()
        t.sety(window_height//2)
        t.setheading(270)
        for _ in range(window_height//20):
            t.down()
            t.forward(10)
            t.up()
            t.forward(10)

