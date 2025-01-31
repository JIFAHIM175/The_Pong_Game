from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
      super().__init__()
      self.color("white")
      self.penup()
      self.hideturtle()
      self.l_score = 0
      self.r_score = 0
      self.goto(-100, 220)
      self.write(f"{self.l_score}", align="center", font=("Courier", 50, "normal"))
      self.goto(100, 220)
      self.write(f"{self.r_score}", align="center", font=("Courier", 50, "normal"))
