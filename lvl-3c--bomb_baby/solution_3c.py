import sys
from memory_profiler import profile


import math

@profile(precision=4)
def answer(M, F):
  a = int(M)
  b = int(F)
  return find(a, b)

def find(a, b):
  count = 0
  while 1:
    if a == 1 and b == 1:
      return str(count) # return result
    if a <= 0 or b <= 0 or a == b:
      return 'impossible'

    a, b = enforce_a_greater_than_b(a, b)
    count += (a / b)
    a %= b
    if b == 1:
      a = 1
      count -= 1

def enforce_a_greater_than_b(a, b):
  if a < b:
    a, b = b, a # swap
  return a, b



result = answer( sys.argv[1], sys.argv[2] )
print 'RESULT: ', result
