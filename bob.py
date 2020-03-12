
import turtle 


wn = turtle.Screen()
wn.bgcolor("#00ffff") 

bob = turtle.Turtle()
bob.width(0.001)
bob.shape("turtle")
bob.color("red")
bob.goto(0,0)
bob.hideturtle()
bob.speed(0)

for i in range(60):
    
    bob.forward(90)
    bob.left(20)
    bob.color("gold")
    bob.backward(90.5)
    bob.right(242)
    bob.forward(1)
    bob.color("white")
    bob.left(5)
    bob.backward(10)
    bob.right(5)
    bob.forward(10)
    bob.color("black")
    bob.left(20)
    bob.forward(45)
    bob.right(20)
    bob.backward(45)
    bob.color("red") 





bob.penup()
bob.goto(-150,150)

for i in range (60):
    
    bob.pendown()
    bob.color("white")
    bob.left(21)
    bob.forward(15)
    bob.right(21)
    bob.backward(23)
    bob.forward(25)
    bob.color("red")
    bob.left(60.55)
    bob.backward(20)
    bob.left(129)
    bob.forward(43)
    bob.color("gold")
    bob.right(215)
    bob.backward(45)
    bob.left(1)
    bob.forward(7)
    bob.forward(27.5)
    bob.color("purple")
    bob.forward(27.5)
    
bob.penup()
bob.goto(225,-225)
bob.pendown()
for i in range( 45):
    bob.color("red")
    bob.left(30)
    bob.forward(35)
    bob.right(30)
    bob.color("white")
    bob.backward(20)
    bob.left(120)
    bob.color("purple")
    bob.forward(22.5)
    bob.color("gold")
    bob.forward(22.5)
    bob.left(2)

bob.penup()
bob.goto(175,150)
bob.pendown()
for i in range(30):
    bob.forward(70)
    bob.right(55)
    bob.color("#800000")
    bob.forward(57)
    bob.right(45)
    bob.backward(46)
    bob.color("#203080")
    bob.left(1.5)
    bob.forward(30)
    bob.left(170)
    bob.forward(45)
    bob.color("gold")
    bob.left(7)
    bob.backward(40)


    
wn.exitonclick()