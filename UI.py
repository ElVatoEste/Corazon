
import turtle
from time import sleep  
lapiz = turtle.Turtle()
lapiz.width(2)

def curva():
    lapiz.speed(0)
    for x in range(200):
        lapiz.right(1)
        lapiz.forward(1)

def relleno():
    lapiz.speed(0)
    lapiz.fillcolor('red')
    lapiz.begin_fill()
    lapiz.left(140)
    lapiz.forward(113)
    curva()
    lapiz.left(120)
    curva()
    lapiz.forward(112)
    lapiz.end_fill()

def texto():
    lapiz.speed(0)
    lapiz.up()
    lapiz.setpos(-48, 95)
    lapiz.down()
    lapiz.color("purple")
    lapiz.write("Te Quiero", font =(
        "Verdana", 12, "bold"))

relleno()
texto()
lapiz.ht()
sleep(200)

