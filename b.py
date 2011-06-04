import sys

def result(n, pd, pg):
  if pg == 0 and pd != 0:
    return 'Broken'
  elif pg == 100 and pd != 100:
    return 'Broken'
  if pd & 1 == 0:
    pd >>= 1
  if pd & 1 == 0:
    pd >>= 1
  if pd % 5 == 0:
    pd = pd / 5
  if pd % 5 == 0:
    pd = pd / 5
  return 'Possible' if pd <= n else 'Broken'

t = int(sys.stdin.readline())
for i in xrange(0, t):
  n, pd, pg = sys.stdin.readline().split()
  print result(int(n), int(pd), int(pg))
