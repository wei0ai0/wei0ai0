#蟒蛇
import turtle
turtle.setup(800,350,300,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor("green")
turtle.seth(-40)
for i in range (5):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
