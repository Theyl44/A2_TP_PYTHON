import turtle

turtle.setup(500, 500)
turtle.title('Titre de la fenêtre')
turtle.speed('slowest')
turtle.fillcolor('green')
turtle.begin_fill()
turtle.down()
for i in range(0, 3):
    turtle.forward(10)
    turtle.left(90)
turtle.up()
turtle.end_fill()

turtle.exitonclick()

