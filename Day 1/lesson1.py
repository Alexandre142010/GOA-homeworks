print("Aleqsandre Midelashvili")

from turtle import*

#we want to paint a house

#step 1: draw a square
speed(10)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(60)
color("yellow")

left(90)
forward(90)

right(90)
forward(90)

right(90)
forward(90)
end_fill()
#end of a door

#draw a roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(120)
forward(120)
left(61)
forward(115)
end_fill()
#end of a roof

#draw a window
begin_fill()
penup()
goto(170, 140)
pendown()

right(31)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
left(90)
forward(20)
end_fill()

penup()
goto(70,140)
pendown()
begin_fill()
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
left(90)
forward(20)
end_fill()
#end of a window



exitonclick()