import sys
import pdb

import math

def answer(l, t):
  i = 0
  while i < len(l):
    j = qualified(l, i, t)
    if j >= 0:
      return [i, j]
    i += 1
  return [-1, -1]


def qualified(l, i, t):
  sum = 0
  j = i

  while j < len(l):
    sum += l[j]
    if sum == t:
      return j
    if sum > t:
      return -1
    j += 1
  return -1




# input = int(sys.argv[1])
input = [4, 3, 5, 7, 8]
print(answer( input, 12 ))
