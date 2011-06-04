''' 
A backtracking for the horse on a chess board problem.
Jumps to each of the possible squares where the number of exits is minimal.
Prints number of solutions found with this constraint,
number of times it went back and the first path that blocked 
'''

import sys

def abort():
  sys.exit(0)
  # pass

# vecini
v = dict()
for i in xrange(0, 64):
  l, c = i / 8, i % 8
  v[i] = []
  for l1 in xrange(0, 8):
    for c1 in xrange(0, 8):
      dl = abs(l - l1)
      dc = abs(c - c1)
      if dl + dc == 3 and abs(dl - dc) == 1:
        v[i].append(l1 * 8 + c1)

# board
b = [0]*64

def count_exits(a):
  c = 0
  for n in v[a]:
    if b[n] == 0:
      c += 1 
  return c

# drum  
d = []

sol = 0
back = 0
back_d = [0]*64

# p = point
def jump(p):
  b[p] = 1
  d.append(p)
  me = 8 # min exits
  options = []
  for a in v[p]:
    if b[a] == 1:
      continue
    e = count_exits(a)
    if e < me:
      me = e
      options = [a]
    elif e == me:
      options.append(a)
  if len(options) == 0:
    global sol, back, back, back_d
    if len(d) < 64:
      back += 1
      if len(d) < len(back_d):
        back_d = list(d)
    else:
      sol += 1
  else:
    for o in options:
      jump(o)
  d.remove(p)
  b[p] = 0

jump(0)
print sol, 'solutions'
print back, 'backs'
print back_d
