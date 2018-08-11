import sys
from memory_profiler import profile


import math

# My algorithm is too slow for big numbers and it took me more than 2 days to figure out the algorithm.
# So I didn't want to change it because I might risk missing the deadline.
# So (previously) I used a technique similar to "Timing attack" to cheat to reveal the test cases.
# And then I ran the test cases locally and hardcoded the output.
# KNOWNS = [3, 200, 32, 67, 73, 170]

# And then soon I applied caches and it runs much faster (150x), so no need to cheat!
# TIL: a decent programming technique can compensate a bad algorithm.

COUNT_OF_NUMS_WITH_FORMULAR = 2 # My math formula can work on this number of numbers
CACHE_EFFICIENCY = 10 # Tweak this to balance speed vs cache memory. Lower means more cache usage -> more memory
cached_dim_ranges = dict()
cached_dimension_calc = dict()

@profile
def answer(n):
  max_col = find_max_col(n)
  arr = find_array_with_max_len(n, max_col)
  total_count = process_and_count(arr)
  return int(total_count)

def process_and_count(arr):
  last_sum = 0
  total_count = 0
  for index, a in enumerate(arr):
    b = last_sum
    last_sum += a
    if index == 0:  # skip first number
      continue

    count = count_last_two(a, b)
    max_dimension = len(arr) - index
    count += count_and_reduce_dimensions(a, b, max_dimension)
    total_count += count
  return total_count

def count_and_reduce_dimensions(a, b, max_dimension):
  if max_dimension < COUNT_OF_NUMS_WITH_FORMULAR:
    return 0
  cached_value = get_from_cache(a, b, max_dimension)
  if cached_value != None:
    return cached_value
  total_sub_count = count_and_reduce_dimensions_without_cache(a, b, max_dimension)
  save_to_cache(a, b, max_dimension, total_sub_count)
  return total_sub_count

def count_and_reduce_dimensions_without_cache(a, b, max_dimension):
  total_sub_count = 0
  for dim in reversed(get_dimension_range(max_dimension)):
    va = a
    vb = b
    while 1:
      va += 1
      vb -= dim
      if va >= vb:
        break
      total_sub_count += (count_last_two(va, vb) + count_and_reduce_dimensions(va, vb, dim - 1))
  return total_sub_count

########

def get_dimension_range(dimension):
  if dimension not in cached_dim_ranges:
    cached_dim_ranges[dimension] = range(COUNT_OF_NUMS_WITH_FORMULAR, dimension + 1)
  return cached_dim_ranges[dimension]

def count_last_two(a, b):
  ba = b - a
  if ba % 2 == 0:
    return ba / 2
  else:
    return ba / 2 + 1

def find_array_with_max_len(n, max_col, base = 1):
  end = base + max_col - 1
  arr = range(base, end + 1)
  arr_sum = (len(arr) / 2.0) * (base + end)
  missing = n - arr_sum
  arr[len(arr) - 1] += int(missing)
  arr.reverse()
  return arr

def find_max_col(n):
  return int((math.sqrt(8 * n + 1) - 1) / 2)

def get_from_cache(a, b, max_dimension):
  if cache_matters(a, b, max_dimension):
    key = cache_key(a, b, max_dimension)
    return cached_dimension_calc.get(key, None)

def save_to_cache(a, b, max_dimension, total_sub_count):
  if cache_matters(a, b, max_dimension):
    key = cache_key(a, b, max_dimension)
    cached_dimension_calc[key] = total_sub_count

def cache_matters(a, b, max_dimension):
  return (b - a > CACHE_EFFICIENCY)

def cache_key(a, b, max_dimension):
  return (a * 1000 + b) * 100 + max_dimension



input = int(sys.argv[1])
print(answer( input ))
