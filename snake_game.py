import turtle
import os
import time
import random

delay = 0.1

score = 0
high_score = 0

#Setting he backgorund screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("white")
wn.setup(width = 800, height = 800)
wn.tracer(0) #if its 0 thn it turs off the screen updates, used while loop ahead for this (1)


# wn.mainloop() #it keeps our screen opened (wherever mainloop is the turtle ends)

#SNAKE
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#FOOD
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,360)
pen.write("Score : 0 High Score : 0", align = "center", font = ("Courier", 24, "normal"))




def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


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

#Keyboard Bindings - connects keypress with a particular function
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#(1)
while True:
    wn.update()

    #checking if collison with border
    if head.xcor() > 390 or head.xcor() < -390 or head.ycor() > 390 or head.ycor() < -390:
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "stop"


    if head.distance(food) < 20:
        #Move food to a random spot
        x = random.randint(-390,390)
        y = random.randint(-390,390)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #score
        delay -= 0.001
        score = score + 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {} High Score : {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))
        

    #movinf end segments first -reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segmennt 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    #checkin for head collision with body of the snake
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"
        
            #hiding the segments
            for segment in segments:
                segment.goto(1000,1000)
            
            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Score : {} High Score : {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))
        


    time.sleep(delay)

wn.mainloop()
