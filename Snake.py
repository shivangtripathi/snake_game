## importing turtle for graphics  
import turtle
import time
import random

delay = 0.1

##Score
score=0
high_score=0

## creating the window
wn= turtle.Screen()
wn.title("Snake Game @Shivang_Tripathi")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0) #turn off screen updates

##Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction="stop"

##Snake Food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,90)

segments = [ ]

##Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0    High Score: 0",align="center",font=("Arial",24,"normal"))

##Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
            x = head.xcor()
            head.setx(x+20)

    if head.direction == "left":
            x = head.xcor()
            head.setx(x-20)


##Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

##Main Game loop
while True:
    wn.update()

    #Check for border collision
    if head.xcor()>290 or head.xcor()<(-290) or head.ycor()>290 or head.ycor()<(-290):
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #Hidin Segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segment list
        segments.clear()

        #reset the score
        score=0

        #reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Arial",24,"normal"))

    #Check for Collision with the food
    if head.distance(food)<20:
        #Move the food to random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #Add a segement
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        #Short the delay
        delay -= 0.001
        
        #Increase the score
        score += 10

        if score > high_score:
            high_score=score

        pen.clear()  
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Arial",24,"normal"))  

    #Move the end segemnts first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move the segment 0 to where the head is
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)         

    move()

    #Check for collision with body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop" 

            #hide the segments list
            segments.clear()

            #reset score
            score = 0

            #reset the delay   
            delay=0.1

            #update score
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Arial",24,"normal"))

    time.sleep(delay)  
    
wn.mainloop()          
