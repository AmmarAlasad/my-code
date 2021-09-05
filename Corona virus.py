from turtle import *
Screen()
bgcolor("black")
color("green")
speed(0)
goto(0,200)
size = 0
angle = 0 
i = 0
while True :
    fd(size)
    right(angle)
    size += 3 
    i += 1
    angle += 1
    if angle == 200:
        break
mainloop()