import turtle

def turtle_forward(l, d):
  turtle.forward(l)

def draw(l, d):
  forward = turtle_forward if d >= 5 else draw
  forward(l / 3, d + 1)
  turtle.left(60)
  forward(l / 3, d + 1)
  turtle.right(120)
  forward(l / 3, d + 1)
  turtle.left(60)
  forward(l / 3, d + 1)

turtle.setworldcoordinates(0, 0, 1000, 1000)
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.setpos(10, 400)
turtle.pendown()
draw(990, 1)
turtle.hideturtle()
turtle.exitonclick()
