# Platformer.py
from turtle import Turtle, Screen
import time

wn = Screen()
screen = Screen()

# Make the border
painter = Turtle()
painter.speed(0)
painter.penup()
painter.goto(-300,-300)
painter.pendown()
painter.pensize(3)

# border
for i in range(4):
    painter.forward(600)
    painter.left(90)
painter.hideturtle()

# Make the player 
p = Turtle()
p.speed(0)
p.color("blue")
p.shape("square")
p.penup()
p.setheading(90)
p.speed(0)

# Speed of the player
player_speed = 5

"""
move left and right
"""
# Move left
def move_left():
    x = p.xcor()
    x -= player_speed
    # if it goes out of boundaries
    if x < -290:
        x = -290
    p.setx(x)
    time.sleep(0.01)

# Move right
def move_right():
    x = p.xcor()
    x += player_speed
    # if it goes out of boundaries
    if x > 290:
        x = 290
    p.setx(x)
    time.sleep(0.01)

# Defines speed of falling
gravitySpeed = 0

# Jumping mechanics
def jump():
    y = p.ycor()
    y += 
    # if it goes out of boundaries
    if x < -290:
        x = -290
        gravitySpeed = -1
    p.setx(x)
    time.sleep(0.01)


# Determines when a player can jump (This way the player cannot jump midair)
jumpKey = False
gameWin = False

while(gameWin):
    while (p.ycor > 300):
        jumpKey = False
    if (p.ycor < 300):
        jumpKey = True

    while (jumpKey):

    
    
    # Keys for moving left and right
    wn.listen()
    wn.onkeypress(move_left, "a")
    wn.onkeypress(move_right, "d")

wn.mainloop()