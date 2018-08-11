import pdb



import math
import sys
sys.setrecursionlimit(1500)

def answer(n):
  n = int(n)
  return int(find_steps_count(n, 0)) # don't forget to cast to int. Type matters!

def base_cases(num):
  if num == 3:
    return 2
  elif num == 2:
    return 1
  elif num <= 1:
    return 0
  else:
    return None

def find_steps_count(num, current_count = 0):
  base_result = base_cases(num)
  if base_result != None:
    return current_count + base_result

  current_count = current_count + 1
  if num % 2 == 0:
    return find_steps_count(num / 2, current_count)
  else:
    new_num = (num + 1) if second_last_digit_is_one(num) else (num - 1)
    return find_steps_count(new_num, current_count)

# Check if second last digit in binary is 1
def second_last_digit_is_one(num):
  return (num >> 1) % 2 != 0



result = answer( sys.argv[1] )
print 'RESULT: ', result
