import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



CAR_COUNTER = 0  #to create a car on every 6th loop 
DISTANCE_COLLISION = 20 #the minimum distance b/w car and the player allowed 


#Screen Setup 
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Turtle Crossing') 
screen.listen() 



turtle = Player() #creating the player object 
car = []



score = Scoreboard(turtle.level) #creating the score object 
 

 
 
game_is_on = True
while game_is_on:

    time.sleep(0.05)
    screen.update()
    screen.onkey(fun = turtle.move, key = 'Up')
    
    #Adding car at every 6th iteration 
    CAR_COUNTER = CAR_COUNTER + 1 
    if CAR_COUNTER == 6 : 
        cars= CarManager(turtle.level) 
        car = car +[cars]       
        CAR_COUNTER = 0 
        
    #calculating the level     
    if turtle.level != -1  :score.score_update(score = turtle.level)
        
     
    #movement of the cars 
    for _ in range(0 , len(car) ) :         
            car[_].move() 
            if turtle.player.distance(car[_].car.xcor() , car[_].car.ycor()  ) <= DISTANCE_COLLISION  : 
                     print('lost')
                     turtle.lost()
                
   
            
        
    

    
    
               
            
                
                  
    
    
    
    

