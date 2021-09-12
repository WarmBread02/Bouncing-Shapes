
import turtle
import random
import time

t = turtle.Pen()
turtle.bgcolor('black')
def writeLetter(letter, pos):
    t.color('white')
    t.penup()
    t.setposition(pos, 0)
    t.pendown()
    t.write(letter, font=('Arial', 50, 'normal'))
    time.sleep(0.5)


def title():
    writeLetter('M', -125)
    writeLetter('U', -65)
    writeLetter('S', -15)
    writeLetter('I', 35)
    writeLetter('C', 55)

title()

m = turtle.Screen()
m.bgcolor("black")
m.title("Howdy Hack!")
m.tracer(0)



balls = []
for _ in range(50):
    balls.append(turtle.Turtle())

colors = ['red', 'blue', 'yellow', 'green','purple', 'orange', 'cyan', 'white', 'grey', 'aquamarine', 'cornflowerblue', 'gold']
shapes = ["circle", "triangle", "square", ]

for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(-50,400)
    ball.goto(x,y)
    ball.dy = 0 #direction going down
    ball.dx = random.uniform(-1,1) #direction doing sideways
    ball.da = random.randint(-3,3)

gravity = 0.01 #AKA acceleration

while True:
    m.update()
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)

        #wall collision
        if ball.xcor() > 375:
            ball.dx *= -1
            ball.da *= -1

        if ball.xcor() < -375:
            ball.dx *= -1
            ball.da *= -1

        #bouncing
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
            ball.da *= -1

    #collisions between shapes
    for i in range(0, len(balls)):
        for j in range(i + 1, len(balls)):
            #check for collision
            if balls[i].distance(balls[j]) < 20:
                temp_dx = balls[i].dx
                temp_dy = balls[i].dy

                balls[i].dx = balls[j].dx
                balls[i].dy = balls[j].dy

                balls[j].dx = temp_dx
                balls[j].dy = temp_dy





m.mainloop()