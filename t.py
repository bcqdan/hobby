import turtle

bs = 100
font = ('Arial', 60, 'normal')
path = [0, 10, 4, 14, 31, 46, 63, 53, 59, 49, 32, 17, 2, 8, 25, 40, 57, 42, 48, 58, 52, 62, 47, 30, 15, 5, 11, 1, 16, 33, 43, 60, 54, 39, 22, 7, 13, 23, 6, 21, 36, 19, 9, 26, 20, 3, 18, 12, 27, 37]
pos = 0

def rect(x, y):
  turtle.seth(0)
  turtle.pu()
  turtle.setpos(x*bs, y*bs)
  turtle.pd()
  color = 'black' if (x + y) % 2 == 0 else 'white'
  turtle.color('black')
  turtle.fillcolor(color)
  turtle.begin_fill()
  for i in xrange(3):
    turtle.forward(bs)
    turtle.left(90)
  turtle.end_fill()

def horse(x, y):
  c = unichr(0x265E).encode('utf-8')
  turtle.pu()
  turtle.setpos(x*bs+50, y*bs+25)
  turtle.color('red')
  turtle.write(c, True, 'center', font)

def board():
  for i in xrange(8):
    for j in xrange(8):
      rect(i, j)
  turtle.pu()
  
turtle.clear()
turtle.setworldcoordinates(0, 0, 8*bs, 8*bs)
#turtle.ht()
#turtle.speed(0)

def next():
  global pos
  if pos < len(path):
    p = path[pos]
    horse(p / 8, p % 8)
    pos += 1

board()
next()
turtle.onkey(next, 'space')
turtle.listen()
turtle.exitonclick()
