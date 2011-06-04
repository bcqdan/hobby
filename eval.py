''' Simple expression evaluator '''

# expr = term | term + expr
# term = factor | factor * term
# factor = constant | (expr)

import sys
import traceback

class iter:
  def __init__(self, s, p):
    self.s = s
    self.p = p

  def current(self):
    return self.s[self.p]

  def next(self):
    self.p += 1

  def done(self):
    return self.p == len(self.s)

def isdigit(c):
  return c in '0123456789'

def fail(it):
  print 'Error at char: %d, (%s)' % (it.p, it.current())
  traceback.print_stack()
  sys.exit(0)

def expr(it):
  value = term(it)
  if it.done() or it.current() == ')':
    return value
  elif it.current() == '+':
    it.next()
    return value + expr(it)
  else:
    fail(it)

def term(it):
  value = factor(it)
  if it.done() or it.current() == '+' or it.current() == ')':
    return value
  elif it.current() == '*':
    it.next()
    return value * term(it)
  else:
    fail(it)

def factor(it):
  c = it.current()
  if c == '(':
    it.next()
    value = expr(it)
    if it.current() != ')':
      fail(it)
    else:
      it.next()
      return value
  elif isdigit(c):
    return constant(it)
  else:
    fail(it)

def constant(it):
  value = int(it.current())
  it.next()
  while not it.done() and isdigit(it.current()):
    value = value * 10 + int(it.current())
    it.next()
  return value

def myeval(s):
  return expr(iter(s, 0))

def check(s):
  return eval(s) == myeval(s)

# main
print check('1')
print check('1+2')
print check('2*3')
print check('1+2*3')
print check('1+2*5+3*3')
print check('(1+2*3)+4')
print check('1+(1+1)*5+3*(1+2)')
print check('45*10+2*(2+8)+8')
print check('1+1*2+1*2*3*0+99+(1+2)')
print check('(5+6)*(9*10)')
print check('(((2+3)*4)+1)*100')
