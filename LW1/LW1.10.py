import turtle

a = int(input())
x = 1

def print():
    turtle.stamp()
    
while x < a:
    turtle.forward(100)
    turtle.up()
    turtle.backward(100)
    turtle.left(40)
    turtle.down()
    x+=1
