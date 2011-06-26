''' Generate a random string of length sys.arg[1] '''
import sys
import random

l = int(sys.argv[1])
r = random.Random()

s = ''
for i in xrange(l):
  s += chr(r.randint(ord('a'), ord('z')))

print s
