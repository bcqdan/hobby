import turtle as t
t.setworldcoordinates(0, 0, 1000, 1000)
t.speed(0)
#t.ht()

def turtle_forward(l, d):
  t.forward(l)

def draw(l, d):
  forward = turtle_forward if d >= 5 else draw
  forward(l / 3, d + 1)
  t.left(90)
  forward(l / 3, d + 1)
  t.right(90)
  forward(l / 3, d + 1)
  t.right(90)
  forward(l / 3, d + 1)
  t.left(90)
  forward(l / 3, d + 1)

t.pu()
t.setpos(10, 400)
t.pd()
draw(990, 1)
t.ht()

t.exitonclick()
