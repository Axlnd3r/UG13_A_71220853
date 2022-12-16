import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.shape ("square")
t.speed(speed=0)
t.pensize(10)
t.color('purple')
t.hideturtle()

#M
t.penup()
t.goto(-300,50)
t.pendown()
t.right(90)
t.forward(150)
t.backward(150)

t.left(45)
t.forward(90)

t.left(95)
t.forward(90)

t.right(140)
t.forward(150)
t.penup()
t.goto(150,-5)

#8
t.goto(-110,0)
t.left(90)
t.pendown()
t.circle(30)
t.circle(-50)
t.penup()

#5
t.goto(-30,0)
t.pendown()
t.left(90)
t.forward(50)
t.right(90)
t.forward(60)
t.penup()
t.goto(-30,0)
t.pendown()
t.forward(20)
t.circle(-50,180)
t.forward(20)
t.penup()

#3
t.goto(70,50)
t.pendown()
t.right(180)
t.forward(70)
t.right(130)
t.forward(90)
t.left(130)
t.forward(20)
t.circle(-50,180)
t.forward(20)





s.exitonclick()