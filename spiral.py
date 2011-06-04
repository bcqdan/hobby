import turtle as t

t.setworldcoordinates(0, 0, 1000, 1000)
t.speed(0)
t.pu()
t.color('black')
t.setpos(750, 500)
t.pd()
angle = 90
d = 10
while True:
  t.forward(d)
  t.left(angle)
  angle -= 0.1
  if t.pos()[0] > 1000:
    break

t.exitonclick()

