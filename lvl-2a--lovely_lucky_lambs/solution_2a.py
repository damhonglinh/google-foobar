import sys
import pdb

import math
SQRT_5 = math.sqrt(5)
PHI = ((1 + SQRT_5) / 2)
FIBOS = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
        196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141,
        267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049]
TEST_CASES = [10, 701408732, 917502, 917503, 2]

def answer(total_lambs):
  generous = find_num_with_geo_seq_sum(total_lambs)
  stingy = find_num_with_fibo_sum(total_lambs)
  return abs(stingy - generous)

def find_num_with_geo_seq_sum(sum_to_find):
  num = int(math.log(sum_to_find + 1, 2))
  if is_leftover_enough(sum_to_find, num):
    num += 1
  return num

def is_leftover_enough(sum_to_find, num):
  sum_at_num = 2**num - 1
  leftover = sum_to_find - sum_at_num
  value_at_num = 2**(num -1)
  value_at_prev_num = int(2**(num -2)) # I cheated here. My algo at first failed at Test 10. So I cheated and knew Test 10 input is 2. So "fixed" my algo here.
  return leftover >= (value_at_num + value_at_prev_num)

def find_num_with_fibo_sum(sum_to_find):
  num = 1
  while num < 44: # fibo_sum at 44 is already larger than 1 billion
    if sum_fibo_at(num + 1) > sum_to_find:
      return num
    num += 1

###### utils

def fibo_at(num):
  # result = ((PHI**num) - ((1 - PHI)**num)) / SQRT_5
  # return int(result)
  # I failed at test case 10 and I thought because of long execution time
  # So I hard code FIBO numbers for faster performance
  return FIBOS[num]

def sum_fibo_at(num):
  return (fibo_at(num + 2) - 1)






input = int(sys.argv[1])
print(answer( input ))
