import turtle

def drawLine(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90) 
    
def drawDight(number):
    drawLine(True) if number in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if number in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if number in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if number in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if number in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if number in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if number in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(80)
    
def drawDate(data):
    for i in data:
        drawDight(eval(i))

turtle.penup()
turtle.fd(-300)
drawDate("20200510")
n=eval(input())