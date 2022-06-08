from turtle import width
# this library help me draws forms and animated it بترسم الاشكال
import turtle

wind = turtle.Screen()
wind.title("ping pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)


# madrib1
madrib1 = turtle.Turtle()  # initializes turtle object(shape)
# دي مش سرعة المضرب ولكن دي السرعه ال  turtle module بيرسم بهاالمضرب علي الشاشه كل مايتحرك علشان نقدر نشوفه
madrib1.speed(0)
# 0 >> معناها عايز شكل المضرب يترسم او يتحدد علي الشاشه باقصي سرعه علشان محسش بالفرق
madrib1.shape("square")
madrib1.color("blue")
madrib1.shapesize(stretch_wid=6, stretch_len=1)
madrib1.penup()  # stops the object from drawing lines
madrib1.goto(-350, 0)

# madrib2
madrib2 = turtle.Turtle()
madrib2.speed(0)
madrib2.shape("square")
madrib2.color("green")
madrib2.shapesize(stretch_wid=6, stretch_len=1)
madrib2.penup()  # no lines because turtle
madrib2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()  # no lines because turtle
ball.goto(0, 0)
ball.dx = 0.5  # direction of ball horizontal
ball.dy = 0.5  # direction of ball vertical

# score
score_p1 = 0
score_p2 = 0
score = turtle.Turtle()
score.speed(0)  # speed of animation on screen
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player1: 0   Player2: 0", align="center",
            font=("Courier", 20, "normal"))

# functions


def madrib1_up():
    y = madrib1.ycor()  # get the Y coordinate of madrib
    y += 20
    madrib1.sety(y)


def madrib1_down():
    y = madrib1.ycor()
    y -= 20
    madrib1.sety(y)


def madrib2_up():
    y = madrib2.ycor()
    y += 20
    madrib2.sety(y)


def madrib2_down():
    y = madrib2.ycor()
    y -= 20
    madrib2.sety(y)


# keyboard bindings
wind.listen()  # tell the window to expect keyboard input
wind.onkeypress(madrib1_up, "w")
wind.onkeypress(madrib1_down, "s")

wind.onkeypress(madrib2_up, "Up")
wind.onkeypress(madrib2_down, "Down")


# main game loop
while True:
    wind.update()  # updates the screen everytime the loop run

    # move the ball
    # xcor coordinate postion of ball in now + rate of changing
    # ball starts at 0 and everytime loops run>> +0.5 x axis size of ball >> 20*20 pixel
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check, top border +300px, bottom border -300px, ball 20px
    if ball.ycor() > 290:    # top position of ball now >290
        ball.sety(290)
        ball.dy *= -1        # The ball is moving in the opposite direction by -0.5

    if ball.ycor() < -290:  # bottom position of ball now >290
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:  # right border position of ball now >390
        # ball.setx(390)
        ball.goto(0, 0)
        ball.dx *= -1
        score_p1 += 1
        score.clear()
        score.write("Player1: {}   Player2: {} ".format(score_p1, score_p2), align="center",
                    font=("Courier", 20, "normal"))

    if ball.xcor() < -390:  # left border
        # ball.setx(-390)
        ball.goto(0, 0)
        ball.dx *= -1
        score_p2 += 1
        score.clear()
        score.write("Player1: {}   Player2: {} ".format(score_p1, score_p2), align="center",
                    font=("Courier", 20, "normal"))

    # borders of madribs
    if madrib1.ycor() > 230:
        madrib1.sety(230)

    if madrib1.ycor() < -230:
        madrib1.sety(-230)

    if madrib2.ycor() > 230:
        madrib2.sety(230)

    if madrib2.ycor() < -230:
        madrib2.sety(-230)

    # tasadom madrib with ball
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrib2.ycor()+40 and ball.ycor() > madrib2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrib1.ycor()+40 and ball.ycor() > madrib1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
