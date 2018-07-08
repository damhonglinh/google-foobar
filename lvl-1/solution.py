import sys
import pdb


def answer(s):
  input = s
  divs = find_divisors(len(input))

  for div in divs:
    if qualified(input, div):
      return (len(input) / div)
  None

def qualified(input, div):
  offset = 0
  while offset < div:
    if qualified_circle(input, div, offset):
      return True
    offset += 1
  return False

def qualified_circle(input, div, offset):
  base_str = input[offset:(div + offset)]
  i = div + offset
  while i < len(input):
    next_i = i + div
    sub_str = input[i:next_i]
    if sub_str != base_str:
      return False
    i = next_i
  return True

###### utils

def find_divisors(n):
  result = []
  for i in range(1, n + 1):
    if n % i == 0:
      result.append(i)
  return result



print(answer(sys.argv[1]))
