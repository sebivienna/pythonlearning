import random
import turtle

turtle.bgcolor("yellow")
turtle.speed(3)
turtle.pensize(10)

turtle.circle(-18)
for x in range(0,1000,30):
	turtle.circle(x)
turtle.speed(3)
turtle.clear()
turtle.pensize(3)
turtle.bgcolor("darkgreen")

for x in range(8):
	turtle.fd(100)
	turtle.left(135)
	
	
	
turtle.done()

