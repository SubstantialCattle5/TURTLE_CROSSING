from turtle import Turtle 

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self): 
        self.score_pen = Turtle()
        self.score_pen.speed(0)
        self.score_pen.color("black")        
    
    def score_update(self , score) : 
        self.score_pen.clear()
        self.score_pen.st() 
        self.score_pen.penup()
        self.score_pen.goto(-290,260)
        self.score_pen.pendown()
        self.score_pen.write(f'Level: {score} ',align="left", font=FONT)
        self.score_pen.hideturtle()
         
         
