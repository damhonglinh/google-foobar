# Challenge description
```
Bomb, Baby!
===========

You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time.

But there's a few catches. First, the bombs self-replicate via one of two distinct processes:
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle.

Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good!

And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!)

You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function answer(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the answer would be "1". However, if M = "2" and F = "4", it would not be possible.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) M = "2"
    (string) F = "1"
Output:
    (string) "1"

Inputs:
    (string) M = "4"
    (string) F = "7"
Output:
    (string) "4"
```


# Notes

This challenge is quite straightforward so there is nothing special.

# Algorithm summary:

+ Loop inputs descendingly, from (M,F) to (1,1).
+ So that the problem is narrowed down to finding the next possible pair (descendingly)
+ Let (a0,b0) be (M,F) and (a1,b1) be the next numbers of (a0,b0), descendingly
+ If a0 > b0: b1 must be equal to b0, therefore, a1 = a0 - b0
+ If a0 < b0: a1 must be equal to a0, therefore, b1 = b0 - a0
+ If a0 == b0: impossible
+ Loop until: if a1 == 0 AND b1 == 0, then result
+ Or loop until: if a1 <= 0 OR b1 <= 0, then result is impossible

Optimize: substracting is slow. So using divide and MOD is faster.

## Pseudo code:
```ruby
  count = 0
  while true:
    return count        if a == 1 and b == 1
    return 'impossible' if a <= 0 or b <= 0 or a == b
    if a > b:
      a = a - b
    else:
      b = b - a
    count += 1
```
