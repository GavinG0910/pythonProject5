import turtle
import random
screen = turtle.Screen()
screen.screensize(500,500)
screen. bgcolor("black")

t = turtle.Turtle()
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("white")
t.write('Background color',font=("arial",30,"bold"),align="center")


t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor("Tan")
t.write('1.  Tan',font=("arial",30,"bold"),align="left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor("Azure")
t.write('2.  Azure',font=("arial",30,"bold"),align="left")


t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor("Aquamarine")
t.write('3.  Aquamarine',font=("arial",30,"bold"),align="left")

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor("Darkkhaki")
t.write('4.  Darkkhaki',font=("arial",30,"bold"),align="left")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor("white")
t.write('Choose a Color',font=("arial",30,"bold"),align="center")
choice = int(input('Choose a color:'))
if choice == 1:
    screen. bgcolor("tan")
elif choice == 2:

    screen. bgcolor("azure")
elif choice == 3:
    screen. bgcolor("aquamarine")
else:
    screen.bgcolor('darkkhaki')
t.clear()
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("black")
t.write('Enter your name',font=("arial",30,"bold"),align="center")
name=input("Enter your name;")
t.clear()
operation = random.randint(1,4)
if operation ==1:
    symbol = "+"
 #add
# num1=int(input("Enter a number;"))
# num2=int(input("Enter another number;"))

    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    solution = num1 + num2
elif operation ==2:
    symbol = "-"
    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    solution = num1 - num2
elif operation ==3:
    symbol = "*"
    
    num1 = random.randint(-10,10)
    num2 = random.randint(-10,10)
    solution = num1 * num2
elif operation ==4:
    symbol = "/"

    num1 = random.randint(-10,10)
    num2 = random.randint(1,10)
    sign = random.randint(1,2)
    if sign == 2:
        num2 = -1*num2
    solution = num1 / num2
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("red")
t.write(name,font=("arial",30,"bold"),align="center")


t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("red")
t.write(num1,font=("arial",30,"bold"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor("green")
t.write(symbol,font=("arial",30,"bold"),align="center")
t.penup()
t.goto(0,0)
t.pendown()
t.write(num2,font=("arial",30,"bold"),align="center")


t.penup()
t.goto(100,0)
t.pendown()
t.pencolor("red")
t.write("=",font=("arial",30,"bold"),align="center")


answer=float(input("Enter the answer: "))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor("red")
t.write(solution,font=("arial",30,"bold"),align="center")



t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor("red")
t.write("your answer: "+str(answer),font=("arial",30,"bold"),align="center")

if answer == solution:

    screen.bgcolor("dodgerblue")
    t.penup()
    t.goto(0,100)
    t.pendown()
    t.pencolor("red")
    t.write("Good Job:",font=("arial",30,"bold"),align="center")

else:

    screen.bgcolor("darkorange")
    t.penup()
    t.goto(0,100)
    t.pendown()
    t.pencolor("red")
    t.write("wrong",font=("arial",30,"bold"),align="center")
turtle.done()