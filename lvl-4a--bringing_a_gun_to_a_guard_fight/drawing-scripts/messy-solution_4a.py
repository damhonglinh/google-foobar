import sys
from termcolor import colored, cprint
#def answer(dimensions, ur_position, guard_position, distance):
def debug(*objects): print(objects)

dims = [3, 2]
ur_pos = [1, 1]
g_pos = [2, 1]
dist = 4

# dims = [300, 275]
# ur_pos = [150, 150]
# g_pos = [185, 100]
# dist = 500

# dims = [1000, 1000]
# ur_pos = [250, 25]
# g_pos = [257, 49]
# dist = 25

dims = [42, 59]
ur_pos = [34, 44]
g_pos = [6, 34]
dist = 5000

##############################################
# def simulate_slow():
#   count = 100000000
#   for i in range(0, count):
#     math.atan(count + i)
##############################################
##############################################

import math
from decimal import Decimal
# def debug(*objects): 1

guard_angles = dict()
your_angles = set()

def answer(dims, ur_pos, guard_pos, dist):
  room_x_count = int(dist / dims[0]) + 1
  room_y_count = int(dist / dims[1]) + 1
  r_square = dist * dist
  total_count = []

  for room_y_idx in range(0, room_y_count + 1):
    for room_x_idx in range(0, room_x_count + 1):
      quadrants = set([ (room_x_idx, room_y_idx), (room_x_idx, -room_y_idx),
                        (-room_x_idx, room_y_idx), (-room_x_idx, -room_y_idx) ])
      for room_index in quadrants:
        total_count.append( check_room(room_index, dims, ur_pos, guard_pos, r_square) )

  total_count = [x for x in total_count if x is not None]
  # debug(total_count)
  result = len(total_count)
  return result

def check_room(room_index, dims, ur_pos, guard_pos, r_square):
  mirr_guard_pos = get_mirror_pos(room_index, dims, guard_pos)
  mirr_ur_pos = get_mirror_pos(room_index, dims, ur_pos)
  guard_in_circle = is_in_circle(ur_pos, mirr_guard_pos, r_square)
  your_in_circle = is_in_circle(ur_pos, mirr_ur_pos, r_square)
  mirr_guard_angle = get_angle(ur_pos, mirr_guard_pos)
  mirr_your_angle = get_angle(ur_pos, mirr_ur_pos)
  # debug('Room Idx:', room_index, '- Mirr Guard:', mirr_guard_pos,
  #      '- Mirr Your:', mirr_ur_pos, '- Guard In Circle:', guard_in_circle)

  if your_in_circle and tuple(ur_pos) != mirr_ur_pos:
    # debug('Room:', colored(room_index, 'yellow'), 'Your Angle:', colored(mirr_your_angle, 'magenta'))
    if (guard_in_circle and mirr_guard_angle not in guard_angles and
        mirr_guard_angle == mirr_your_angle and
        mirr_guard_is_closer(ur_pos, mirr_guard_pos, mirr_ur_pos) ):
      guard_angles[mirr_guard_angle] = mirr_guard_angle
      your_angles.add(mirr_your_angle)
      return mirr_guard_pos
    your_angles.add(mirr_your_angle)

  if guard_in_circle:
    if mirr_guard_angle in your_angles:
      # debug(colored('Hit self: Room:', 'cyan'), colored(room_index, 'yellow'), 'Angle:', mirr_your_angle)
      return None
    if mirr_guard_angle not in guard_angles:
      guard_angles[mirr_guard_angle] = mirr_guard_angle
      return mirr_guard_pos
  return None

def get_mirror_pos(room_index, dims, orig_pos):
  room_x_pos = room_index[0] * dims[0]
  room_y_pos = room_index[1] * dims[1]
  mirr_x = orig_pos[0]
  mirr_y = orig_pos[1]
  if room_index[0] & 1: # check is odd
    mirr_x = dims[0] - orig_pos[0] # flip position as in mirror
  if room_index[1] & 1:
    mirr_y = dims[1] - orig_pos[1]
  return (mirr_x + room_x_pos, mirr_y + room_y_pos)

def is_in_circle(o_pos, x_pos, r_square):
  dx = abs(x_pos[0] - o_pos[0])
  dy = abs(x_pos[1] - o_pos[1])
  return (dx*dx + dy*dy <= r_square)

def get_angle(o_pos, point_pos):
  angle = math.atan2(Decimal(point_pos[1] - o_pos[1]) , Decimal(point_pos[0] - o_pos[0]))
  # debug('Guard Pos:', point_pos, '- Angle: ', angle)
  return angle

def mirr_guard_is_closer(o_pos, mirr_guard_pos, mirr_ur_pos):
  mirr_guard_distance = abs(mirr_guard_pos[0] - o_pos[0]) ** 2 + abs(mirr_guard_pos[1] - o_pos[1]) ** 2
  mirr_ur_distance = abs(mirr_ur_pos[0] - o_pos[0]) ** 2 + abs(mirr_ur_pos[1] - o_pos[1]) ** 2
  debug('mirr_guard_pos: ', mirr_guard_pos)
  return mirr_guard_distance <= mirr_ur_distance


result = answer( dims, ur_pos, g_pos, dist )
debug(colored(('RESULT: ', result), 'green'))
