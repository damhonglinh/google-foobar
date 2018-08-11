# Import the necessary packages and modules
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np

ori_xs = np.array([1, 3])
ori_ys = np.array([1, 2])
width = 4
height = 4
dist = 7

def main_grid(radius, x_count, y_count):
  xc = x_count; yc = y_count
  width = x_count * 2 + 1
  height = y_count * 2 + 1
  grid2d = np.full((width, height, 3), 0.8)
  process_2d_grid(grid2d, radius, xc, yc)
  extend = [0, width, 0, height] # [-x_count, x_count, -y_count, y_count]
  plt.imshow(grid2d, origin='lower', extent=extend)

def process_2d_grid(grid2d, radius, xc, yc):
  putpixel(grid2d, xc, yc)
  x = 0
  y = radius
  dist = 3 - 2 * radius
  while (y >= x):
    draw_circle_pixel(grid2d, xc, yc, x, y)
    x += 1
    if (dist > 0):
      y -= 1
      dist = dist + 4 * (x - y) + 10
    else:
      dist = dist + 4 * x + 6
    draw_circle_pixel(grid2d, xc, yc, x, y)

  return grid2d


def draw_circle_pixel(grid2d, xc, yc, x, y):
  putpixel(grid2d, xc+x, yc+y)
  putpixel(grid2d, xc-x, yc+y)
  putpixel(grid2d, xc+x, yc-y)
  putpixel(grid2d, xc-x, yc-y)
  putpixel(grid2d, xc+y, yc+x)
  putpixel(grid2d, xc-y, yc+x)
  putpixel(grid2d, xc+y, yc-x)
  putpixel(grid2d, xc-y, yc-x)

def putpixel(grid2d, x, y):
  grid2d[x][y] = [0.2, 0.2, 0.2]


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
  plt.savefig('test4.png')
  # plt.show()



# Main flow
room_x_count = dist / width + 1
room_y_count = dist / height + 1
main_grid(dist, int(dist), int(dist))

setup_plot()
