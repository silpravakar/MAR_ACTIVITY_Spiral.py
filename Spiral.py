import turtle

wn=turtle.Screen()
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.hideturtle()

t.color("light yellow")

for i in range(100):
    t.circle(i*2)
    t._rotate(5)
wn.mainloop()
