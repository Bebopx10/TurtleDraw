import turtle
import os
print("Looking in folder:", os.getcwd())


TEXTFILENAME = 'td.txt'
print('TurtleDraw')

TurtleDraw = turtle.Turtle()
TurtleDraw.speed(10)
TurtleDraw.penup()

turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

    
    TurtleDraw.color(color)
    TurtleDraw.goto(x,y)
    TurtleDraw.pendown()

    if (len(parts) == 1):
        TurtleDraw.penup()

    line = turtleDrawTextfile.readline()


turtle.done()
print('\nEnd')