from turtle import *

speed(0)

# Draw petals
for i in range(18):
    penup()
    goto(0, 0)
    seth(i * 20)
    fd(40)
    pendown()
    begin_fill()
    fillcolor("pink")
    circle(70, 60)
    left(120)
    circle(70, 60)
    end_fill()

# Draw center
penup()
goto(-25, 30)
pendown()
begin_fill()
fillcolor("yellow")
circle(40)
end_fill()

# Draw stem
penup()
goto(0, -40)
seth(-90)
pendown()
pensize(5)
pencolor("green")
fd(150)

# Draw leaves
for angle in [-45, 135]:
    penup()
    goto(0, -100)
    seth(angle)
    pendown()
    begin_fill()
    fillcolor("green")
    circle(30, 90)
    left(90)
    circle(30, 90)
    end_fill()

done()
