# Import the necessary packages and modules
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np

ori_xs = np.array([1, 2])
ori_ys = np.array([7, 3])
width = 6
height = 8
dist = 19

def draw_room(x, y, w=3, h=2, is_mirror=False):
  plt.bar(x, width=w, height=h, bottom=y, align='edge', fill=False, **style_options(is_mirror))

def draw_agents(x0, y0, xs, ys):
  x = xs + x0
  y = ys + y0
  plt.scatter(x[0], y[0], marker='.')
  plt.scatter(x[-1], y[-1], marker='x')
  draw_shoot_path(x[-1], y[-1])

def draw_shoot_path(guard_x, guard_y):
  x = np.array([ori_xs[0], guard_x])
  y = np.array([ori_ys[0], guard_y])
  # print('X:', x, ' - Y:', y)
  plt.plot(x, y, alpha=0.3)

def draw_room_and_agents(i, j, width, height, xs, ys):
  x0 = j * width
  y0 = i * height
  if j & 1:
    xs = width - xs
  if i & 1:
    ys = height - ys
  draw_room(x0, y0, width, height, True)
  draw_agents(x0, y0, xs, ys)

def main(width, height, xs, ys, room_x_count, room_y_count):
  draw_room(0, 0, width, height, False)
  draw_agents(0, 0, xs, ys)
  for i in range(-room_y_count, room_y_count + 1):
    for j in range(-room_x_count, room_x_count + 1):
      # print('i:', i, ' - j:', j)
      draw_room_and_agents(i, j, width, height, xs, ys)

def draw_circle():
  circle = plt.Circle((ori_xs[0], ori_ys[0]), dist, color='r', zorder=0, fill=False)
  ax = plt.gca()
  ax.add_artist(circle)

# Util

def style_options(is_mirror):
  if is_mirror:
    return dict(linestyle='solid', edgecolor='#222222', zorder=1, alpha=0.5)
  else:
    return dict(linestyle='solid', edgecolor='red', zorder=2, alpha=1.0)

def setup_plot():
  majorLocator = plticker.MultipleLocator(4)
  plt.axes().xaxis.set_major_locator(majorLocator)
  plt.axes().yaxis.set_major_locator(majorLocator)
  minorLocator = plticker.MultipleLocator(1)
  plt.axes().yaxis.set_minor_locator(minorLocator)
  plt.axes().xaxis.set_minor_locator(minorLocator)

  plt.grid(True, color='#f0f0f0', linestyle='-', zorder=0, which='minor')
  plt.axis('equal')
  plt.savefig('test4-full-1.png')
  # plt.show()



# Main flow
room_x_count = dist / width + 1
room_y_count = dist / height + 1
main(width, height, ori_xs, ori_ys, int(room_x_count), int(room_y_count))
draw_circle()

setup_plot()
