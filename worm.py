import sys
import time
import thread
import random
import Tkinter as tk

block_size = 13
bgcolor = '#777964'
fgcolor = 'black'
padding = 10
n, m = 12, 23
width = m * block_size + 2 * padding
height = n * block_size + 2 * padding

root = tk.Tk()
canvas = tk.Canvas(root, width = width, height = height)
canvas.pack()
canvas.create_rectangle( \
    padding - 1, padding - 1, \
    width - padding + 1, height - padding + 1, \
    fill=bgcolor, outline=fgcolor)
r = random.Random()

# table
table = dict()
for i in xrange(n*m):
  table[i] = ' '
tktable = dict()
tkglue = dict()

worm = []
dir = None
events_queue = []
lock = thread.allocate_lock()

goody = 0
tkgoody = None

def abort():
  sys.exit(0)

def death():
  print 'dead'
  abort()

def x(p):
  return (p % m) * block_size + padding

def y(p):
  return (p / m) * block_size + padding

def rectangle(p):
  x1, y1 = x(p) + 1, y(p) + 1
  x2, y2 = x1 + block_size - 2, y1 + block_size - 2
  return x1, y1, x2, y2

def add_head(head):
  table[head] = 'w'
  worm.insert(0, head)
  x1, y1, x2, y2 = rectangle(head)
  tktable[head] = canvas.create_rectangle( \
      x1, y1, x2, y2, fill=fgcolor, outline=fgcolor)
  if len(worm) > 1:
    p = worm[1]
    glue = 0, 0, 0, 0
    if head == p + 1:
      glue = x1-1, y1, x1, y2
    elif head == p - 1:
      glue = x2, y1, x2+1, y2
    elif head == p + m:
      glue = x1, y1-1, x2, y1
    elif head == p - m:
      glue = x1, y2, x2, y2+1
    tkglue[p] = canvas.create_rectangle(glue, outline=fgcolor)

def add_goody():
  global goody, tkgoody
  if len(worm) == n*m:
    death()
  goody = worm[0]
  while table[goody] == 'w':
    goody = r.randint(0, n * m - 1)
  table[goody] = 'g'
  tkgoody = canvas.create_rectangle( \
      rectangle(goody), fill=fgcolor, outline=fgcolor)

def valid(l, c):
  return l >= 0 and l < n and c >= 0 and c < m

def free(l, c):
  return valid(l, c) and (table[l*m + c] != 'w' or worm[len(worm) - 1] == l*m + c)

def advance():
  global worm
  l, c = worm[0] / m, worm[0] % m
  hl, hc = l, c
  if dir == 'right':
    c += 1
  elif dir == 'down':
    l += 1
  elif dir == 'left':
    c -= 1
  elif dir == 'up':
    l -= 1
  else:
    return
  if not free(l, c):
    if not free(hl-1, hc) and not free(hl+1, hc) \
        and not free(hl, hc-1) and not free(hl, hc+1):
      death()
  else:
    next = l * m + c
    if table[next] == 'g':
      canvas.delete(tkgoody)
      add_head(next)
      add_goody()
      print len(worm)
    else:
      remove_tail()
      add_head(next)

def remove_tail():
  if len(worm) > 1:
    tail = worm.pop()
    table[tail] = ' '
    canvas.delete(tktable[tail])
    if tail in tkglue:
      canvas.delete(tkglue[tail])

def procces_event():
  lock.acquire()
  event = events_queue.pop(0)
  global dir
  # use constants
  if event.keycode == 8320768:
    if dir == None or dir == 'left' or dir == 'right':
      dir = 'up'
  elif event.keycode == 8255233:
    if dir == None or dir == 'left' or dir == 'right':
      dir = 'down'
  elif event.keycode == 8124162:
    if dir == None or dir == 'up' or dir == 'down':
      dir = 'left'
  elif event.keycode == 8189699:
    if dir == None or dir == 'up' or dir == 'down':
      dir = 'right'
  lock.release()

def key(event):
  if event.char == 'q':
    sys.exit(0)
  else:
    lock.acquire()
    events_queue.append(event)
    lock.release()
 
def roll():
  heartbeat = 0.12
  t1 = time.time()
  while True:
    if len(events_queue) > 0:
      procces_event()
    advance()
    root.update()
    t1 += heartbeat
    time.sleep(max(0, t1 - time.time()))

for i in xrange(10):
  add_head(n*m/2 + m/2 + i)
add_goody()
thread.start_new_thread(roll, ())
root.bind('<Key>', func=key)
root.tkraise()
tk.mainloop()
