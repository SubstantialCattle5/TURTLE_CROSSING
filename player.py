STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

import turtle 
class Player:
    def __init__(self):
        self.player = turtle.Turtle('turtle')
        self.player.penup()
        self.player.lt(90)
        self.player.color('green')
        self.lost()
        
    def move(self) : 
        self.player.sety(self.player.ycor() + MOVE_DISTANCE)
        
        #to check if the player has crossed the finish line 
        if  self.player.ycor()  > FINISH_LINE_Y : 
            self.player.goto(STARTING_POSITION)
            self.level = self.level + 1
            print(f' Level : {self.level} ' )
            
    def lost(self) :
        self.player.goto(STARTING_POSITION)
        self.level = 0 
            