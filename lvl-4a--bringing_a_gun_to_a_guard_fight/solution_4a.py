import sys
from termcolor import colored, cprint
def debug(*objects): print(objects)
# def debug(*objects): 1

# dims = [300, 275]
# ur_pos = [150, 150]
# g_pos = [185, 100]
# dist = 500

# dims = [42, 59]
# ur_pos = [34, 44]
# g_pos = [6, 34]
# dist = 5000


################################
'''
## Forewords:
+ BUG report: I'm not an advanced Python user (I didn't know Python much, before FooBar challenges),
  but I believe there is a bug in FooBar that global variables are shared across 10 test cases.
  Please see at the end to see more details.
+ Luckily, the test cases don't include an edge case that `distance` = 10_000, and `dimensions` = (2, 3).

## Algorithm summary:
+ This bouncing problem is similar to infinite mirrors effect. This link can illustrate this very well:
  https://gamedev.stackexchange.com/a/154482/117081
+ So, the solution to this bouncing problem can be simplified to couting all those mirrored rooms,
  which are inside a circle with the radius equal to `distance` input.
'''

import math

def set_global_variables(dims, ur_pos, guard_pos, dist):
  global DIMS, UR_POS, GUARD_POS, DIST_SQUARE, HIT_GUARD_ANGLES, HIT_YOU_ANGLES
  DIMS = dims
  UR_POS = ur_pos
  GUARD_POS = guard_pos
  DIST_SQUARE = dist * dist
  HIT_GUARD_ANGLES = dict()
  HIT_YOU_ANGLES = dict()

def answer(dims, ur_pos, guard_pos, dist):
  set_global_variables(dims, ur_pos, guard_pos, dist)
  room_x_count = int(dist / dims[0]) + 1
  room_y_count = int(dist / dims[1]) + 1

  for room_y_idx in range(0, room_y_count + 1):
    for room_x_idx in range(0, room_x_count + 1):
      quadrants = set([ (room_x_idx, room_y_idx), (room_x_idx, -room_y_idx),
                        (-room_x_idx, room_y_idx), (-room_x_idx, -room_y_idx) ])
      for room_index in quadrants:
        check_guard_in_mirrored_room(room_index)

  return len(HIT_GUARD_ANGLES)

def check_guard_in_mirrored_room(room_index):
  mirr_guard_pos = get_mirror_pos(room_index, GUARD_POS)
  mirr_ur_pos = get_mirror_pos(room_index, UR_POS)
  guard_in_circle = is_in_circle(mirr_guard_pos)
  your_in_circle = is_in_circle(mirr_ur_pos)
  mirr_guard_angle = get_angle(mirr_guard_pos)
  mirr_ur_angle = get_angle(mirr_ur_pos)

  if your_in_circle and tuple(UR_POS) != mirr_ur_pos:
    HIT_YOU_ANGLES[mirr_ur_angle] = True
  if guard_in_circle and mirr_guard_angle not in HIT_YOU_ANGLES:
    HIT_GUARD_ANGLES[mirr_guard_angle] = True

def get_mirror_pos(room_index, orig_pos):
  room_x_pos = room_index[0] * DIMS[0]
  room_y_pos = room_index[1] * DIMS[1]
  mirr_x = orig_pos[0]
  mirr_y = orig_pos[1]
  if room_index[0] & 1: # check is odd
    mirr_x = DIMS[0] - orig_pos[0] # flip position as in mirror
  if room_index[1] & 1:
    mirr_y = DIMS[1] - orig_pos[1]
  return (mirr_x + room_x_pos, mirr_y + room_y_pos)

def is_in_circle(x_pos):
  dx = x_pos[0] - UR_POS[0]
  dy = x_pos[1] - UR_POS[1]
  return (dx*dx + dy*dy <= DIST_SQUARE)

def get_angle(x_pos):
  return math.atan2((x_pos[1] - UR_POS[1]), (x_pos[0] - UR_POS[0]))

'''
Below is the codes to reproduce the bug in which global variables are shared in 10 test cases in the same session.
Personal note:
+ I used global variables just to avoid passing around the test's inputs.
  I'm not an advanced Python user so there may be a better approach than using global variables.
+ It was a painful time for me before finding the bug. My codes always failed at test 10. After a massive amount
  of retries and brute force, I found the expected result of test 10 was the same value as my codes' result
  running in my localhost but they still always failed! After more massive amount of retries, and a bit of
  luck, I found it was because of the bug.
+ When my test always failed at test 10, I even suspected that FooBar sandbox somehow used less precision
  in math.atan2 intentionally to trick me (I then confirmed it doesn't); or I even suspected that the hashing algorithm
  in dict() in FooBar sandbox was broken, having collisions so the len of dict() went 'random'.
'''

'''
global_increment_count = 0

def answer(dims, ur_pos, guard_pos, dist):
  global global_increment_count

  test_case_4 = ( dist == 25 and dims[0] == 1000 and dims[1] == 1000
                  and ur_pos[0] == 250 and ur_pos[1] == 25
                  and guard_pos[0] == 257 and guard_pos[1] == 49
                )

  global_increment_count += 1

  # force all test cases (except case 4) to always fail
  if not test_case_4: return -1

  # global_increment_count increments in each test so it reaches to 4 when in test 4.
  if global_increment_count == 4:
    return -1 # enforce test 4 to fail when `global_increment_count` reaches 4
  else:
    return 1 # successful result of test 4. If test 4 passes, then `global_increment_count` does not reach 4

'''


################################

result = answer( dims, ur_pos, g_pos, dist )
debug('RESULT: ', result)
