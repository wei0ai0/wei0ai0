import turtle as t
t.setup(800,700,)
t.bgcolor("black")
t.penup()
t.seth(135)
t.fd(240)
t.seth(90)
t.fd(140)
t.seth(0)
t.pendown()
colors=["red","yellow","blue","green","orange","purple"]
for i in range(361):
    t.pencolor(colors[i%6])
    t.fd(361-i)
    t.right(61)
t.dome()
