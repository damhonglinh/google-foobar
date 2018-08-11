# Challenge description
```
Bringing a Gun to a Guard Fight
===============================

Uh-oh - you've been cornered by one of Commander Lambdas elite guards!

Fortunately, you grabbed a beam weapon from an abandoned guardpost while you were running through the station,
so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the elite guard:
its beams reflect off walls, meaning youll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage.
You also know that if a beam hits a corner, it will bounce back in exactly the same direction.
And of course, if the beam hits either you or the guard, it will stop immediately (albeit painfully).

Write a function answer(dimensions, your_position, guard_position, distance) that gives an array of
2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room,
an array of 2 integers of the guard's x and y coordinates in the room, and returns an integer of the number of
distinct directions that you can fire to hit the elite guard, given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1000, 1 < y_dim <= 1000]. You and the elite guard are both positioned
on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim].
Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.
For example, if you and the elite guard were positioned in a room with dimensions [3, 2], you_position [1, 1],
guard_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the elite guard
(given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2].

As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2]
bounces off the left wall and then the bottom wall before hitting the elite guard with a total shot distance of sqrt(13),
and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite guard with a total shot distance of sqrt(5).

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) dimensions = [3, 2]
    (int list) your_position = [1, 1]
    (int list) guard_position = [2, 1]
    (int) distance = 4
Output:
    (int) 7

Inputs:
    (int list) dimensions = [300, 275]
    (int list) your_position = [150, 150]
    (int list) guard_position = [185, 100]
    (int) distance = 500
Output:
    (int) 9
```


# Notes

This is my favorite challange and this was when I found the bug on FooBar.

This challenge was tricky so I wrote some matplot scripts to draw the rooms. I also wrote the code to reproduce the bug.

# Algorithm summary

+ This bouncing problem is similar to infinite mirrors effect. This link can illustrate this very well:
  https://gamedev.stackexchange.com/a/154482/117081
+ So, the solution to this bouncing problem can be simplified to couting all those mirrored rooms,
  which are inside the circle with the radius equal to `distance` input.

+ It's hard to write texts to explain a visual problem so you can see my drawings to understand more easily.
+ Each rectangle is a mirrored room. The red rectangle is the real room. Each room has a dot
  (your position) and a cross (guard position).
+ Basically, we need to count how many rectangles that have their dot inside the red circle.
+ That's the happy case. To handle edge cases, we need to substract those paths that hit ourselve first, and
those paths that overlap shorter paths.
+ Luckily, there was no edge case that `distance` = 10_000, and `dimensions` = (2, 3).

# The bug

+ The bug is that that global variables are shared across 10 test cases in the same session.
+ I used global variables just to avoid passing around the test's inputs.
  I'm not an advanced Python user so I suspect there is a better approach than using global variables.
+ Finding the bug was a painful time. My codes always failed at test 10.
+ After a massive amount of retries and brute force, I found the expected result of test 10 was
  the same value as my codes' result running in my localhost but they still always failed!
  After more massive amount of retries, and a bit of luck, I found there was a FooBar bug.
+ When my test was always failing at test 10, I even suspected that FooBar sandbox somehow used less precision
  in `math.atan2` intentionally (I then confirmed it doesn't); or I even suspected that the hashing algorithm
  in `dict()` in FooBar sandbox was broken, having collisions so the len of a `dict` went 'random' (I then confirmed it isn't).

## Code to reproduce bug

```ruby
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
    # enforce test 4 to fail when `global_increment_count` reaches 4, meaning there is the bug.
    return -1
  else:
    # `1` is the successful result of test 4.
    # If test 4 passes, then `global_increment_count` does not reach 4, meaning there is no bug.
    return 1
```
