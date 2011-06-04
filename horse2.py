'''
A graphical UI for the horse on the chess board problem.
'''

import sys
import Tkinter as tk

# block size
bs = 80
font = 'courier', 60
# horse char
h = unichr(0x265E)
padding = 20

width = 8 * bs + 2 * padding
height = 8 * bs + 2 * padding
root = tk.Tk()
canvas = tk.Canvas(root, width = width, height = height) 
canvas.pack()

def x(p):
  return (p / 8) * bs + padding

def y(p):
  return (p % 8) * bs + padding

path1 = [0, 10, 4, 14, 31, 46, 63, 53, 59, 49, 32, 17, 2, 8, 25, \
40,57, 42, 48, 58, 52, 62, 47, 30, 15, 5, 11, 1, 16, 33, 43, 60, \
54, 39,  22, 7, 13, 23, 6, 21, 36, 19, 9, 26, 20, 3, 18, 12, 27, 37]

path2 = [0, 10, 4, 14, 31, 46, 63, 53, 47, 62, 52, 58, 48, 33, 16, \
1, 11, 5, 15, 21, 6, 23, 38, 55, 61, 51, 57, 40, 25, 8, 2, 17, 32, \
 42, 59, 49, 34, 24, 9, 3, 18, 12, 27, 44, 29, 19, 36, 26, 41, 56, \
 50, 35, 20, 30, 13, 7, 22, 28, 43, 37, 54, 39, 45, 60]

pos = 0
path = path1

# vecini
v = dict()
for i in xrange(0, 64):
  x1, y1 = i / 8, i % 8
  v[i] = []
  for x2 in xrange(0, 8):
    for y2 in xrange(0, 8):
      dx = abs(x1 - x2)
      dy = abs(y1 - y2)
      if dx + dy == 3 and abs(dx - dy) == 1:
        v[i].append(x2 * 8 + y2)

# board
b = [0]*64

def count_exits(a):
  c = 0
  for n in v[a]:
    if b[n] == 0:
      c += 1 
  return c

def block(p, bg = 'white'):
  x1, y1 = x(p), y(p)
  canvas.create_rectangle(x1, y1, x1 + bs, y1 + bs, fill = bg)

def text(p, text, color):
  xy = x(p) + bs / 2, y(p) + bs / 2
  canvas.create_text(xy, text = text, fill = color, font = font)

def horse(p, color):
  text(p, h, color)

def board():
  for i in xrange(64):
    block(i)

def current():
  n = path[pos]
  block(n)
  horse(n, 'red')
  b[n] = 1
  for i in xrange(64):
    if b[i] == 0:
      block(i)
  for i in v[n]:
    if b[i] == 0:
      exits = count_exits(i)
      if i == path[pos + 1]:
        block(i, 'yellow')
      text(i, str(exits), 'grey')

def next():
  global pos
  if pos < len(path) - 1:
    horse(path[pos], 'black')
    pos += 1
    if pos < len(path):
      current()

def key(event):
  if event.char == ' ':
    next()
  elif event.char == 'q':
    root.destroy()

board()
current()
root.bind('<Key>', func=key)
root.tkraise()
tk.mainloop()
