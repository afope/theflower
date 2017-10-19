import turtle


def draw_shape(some_turtle, radius) :
        some_turtle.circle(radius, 60)
        some_turtle.left(120)
        some_turtle.circle(radius, 60)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("#333")
    petal = turtle.Turtle()
    petal.shape("turtle")
    petal.color("#EC627C")
    petal.speed(10)
    petal.width(2)

    the_petals = 15
    the_radius = 150

    for _ in range(the_petals) :
        draw_shape(petal, the_radius)
        petal.left(360 / the_petals)


    stalk = turtle.Turtle()
    stalk.fill(True)
    stalk.width(3)
    stalk.color("#0FC4E5")
    stalk.shape("turtle")
    stalk.right(90)
    stalk.forward(260)
    stalk.fill(False)
    window.exitonclick()

draw_flower()
draw_shape()
