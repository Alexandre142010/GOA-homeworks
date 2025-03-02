from turtle import*
speed(15)
width(5)
color("green")

#Paint a house


#Step 1: Draw walls
forward(200)
left(90)

forward(120)
left(90)

forward(200)
left(90)
forward(120)


#step 2: draw doors and windows
left(90)
forward(90)
left(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)

penup()
goto(60, 80)
pendown()

color("red")
forward(20)
right(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)

penup()
goto(150, 80)
pendown()
forward(30)
right(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)

#step 3: draw roof
penup()
goto(0,120)
pendown()

right(70)
forward(110)
right(40)
forward(105)
#step 4: draw towers
color("green")
penup()
goto(0,0)
pendown()
right(160)
forward(70)
right(90)
forward(70)
right(90)
forward(70)

penup()
goto(200,70)
pendown()
forward(70)
right(90)
forward(70)
right(90)
forward(70)

#flag
penup()
goto(120,120)
pendown()
forward(120)
color("red")
right(160)
forward(110)
left(70)
forward(50)
left(90)
forward(70)
left(90)
forward(30)
left(90)
forward(70)


exitonclick()