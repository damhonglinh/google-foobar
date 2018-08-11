# Import the necessary packages and modules
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np

# dims = [3, 2]
# ur_pos = [1, 1]
# g_pos = [2, 1]
# dist = 4

dims = [42, 59]
ur_pos = [34, 44]
g_pos = [6, 34]
dist = 5000

ORI_XS = np.array([ur_pos[0], g_pos[0]])
ORI_YS = np.array([ur_pos[1], g_pos[1]])
DIMS = dims
DIST = dist
VIEW_FROM_ROOM_X = 0
VIEW_FROM_ROOM_Y = 0
room_x_count = int(DIST / DIMS[0] + 1)
room_y_count = int(DIST / DIMS[1] + 1)
filename = 'test4-full/test4a--case10.png'

################################
import math
from decimal import Decimal
# def debug(*objects): 1

def draw_room(x, y, is_mirror=False):
  plt.bar(x, width=DIMS[0], height=DIMS[1], bottom=y, align='edge', fill=False, **style_options(is_mirror))

def draw_agents(x0, y0, xs, ys):
  x = xs + x0
  y = ys + y0
  plt.scatter(x[0], y[0], marker='.')
  plt.scatter(x[1], y[1], marker='x')
  # draw_shoot_path(x[1], y[1])

def draw_shoot_path(guard_x, guard_y):
  x = np.array([ORI_XS[0], guard_x])
  y = np.array([ORI_YS[0], guard_y])
  plt.plot(x, y, alpha=0.25)

def draw_room_and_agents(room_index):
  # print('i:', room_index[1], ' - j:', room_index[0])
  is_mirror = room_index[0] != 0 and room_index[1] != 0
  x0 = room_index[0] * DIMS[0] ; y0 = room_index[1] * DIMS[1]
  xs = ORI_XS ; ys = ORI_YS
  if room_index[0] & 1:
    xs = DIMS[0] - xs
  if room_index[1] & 1:
    ys = DIMS[1] - ys
  draw_room(x0, y0, is_mirror=is_mirror)
  draw_agents(x0, y0, xs, ys)

def main(room_x_count, room_y_count):
  for room_y_idx in range(VIEW_FROM_ROOM_Y, room_y_count + 1):
    for room_x_idx in range(VIEW_FROM_ROOM_X, room_x_count + 1):
      draw_room_and_agents((room_x_idx, room_y_idx))
      print('room_x_idx, room_y_idx:', (room_x_idx, room_y_idx))
      draw_room_and_agents((room_x_idx, -room_y_idx))
      draw_room_and_agents((-room_x_idx, room_y_idx))
      draw_room_and_agents((-room_x_idx, -room_y_idx))

def draw_circle():
  circle = plt.Circle((ORI_XS[0], ORI_YS[0]), DIST, color='r', zorder=0, fill=False)
  ax = plt.gca()
  ax.add_artist(circle)

# Util

def style_options(is_mirror):
  if is_mirror:
    return dict(linestyle='solid', edgecolor='#222222', zorder=1, alpha=0.5)
  else:
    return dict(linestyle='solid', edgecolor='red', zorder=2, alpha=1.0)

def setup_plot():
  majorLocator = plticker.MultipleLocator(200)
  majorLocator.MAXTICKS = 10000
  plt.axes().xaxis.set_major_locator(majorLocator)
  plt.axes().yaxis.set_major_locator(majorLocator)
  minorLocator = plticker.MultipleLocator(100)
  minorLocator.MAXTICKS = 10000
  plt.axes().yaxis.set_minor_locator(minorLocator)
  plt.axes().xaxis.set_minor_locator(minorLocator)

  plt.xlim(xmin=(VIEW_FROM_ROOM_X * DIMS[0]))
  plt.ylim(ymin=(VIEW_FROM_ROOM_Y * DIMS[1]))
  plt.grid(True, color='#f0f0f0', linestyle='-', zorder=0, which='minor')
  plt.axis('equal')


# Main flow
def answer():
  main(room_x_count, room_y_count)
  draw_circle()
  setup_plot()


answer()
plt.savefig(filename)
plt.show()
