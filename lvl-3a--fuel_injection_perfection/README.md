### Challenge description
```
Fuel Injection Perfection
=========================
Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP
doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage
while you're at it - so you took the job gladly.
Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need
to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out
the most efficient way to sort and shift the pellets down to a single pellet at a time.
The fuel control mechanisms have three operations:
1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is
cut in half, the safety controls will only allow this to happen if there is an even number of pellets)
Write a function called answer(n) which takes a positive integer as a string and returns the minimum number of operations
needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits
long, so there won't ever be more pellets than you can express in that many digits.
For example:
answer(4) returns 2: 4 -> 2 -> 1
answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (string) n = "4"
Output:
    (int) 2
Inputs:
    (string) n = "15"
Output:
    (int) 5
```


### Notes

+ This is my favorite challenge since I had to go binary to find the solution (although in fact it's not very necessary
to go binary, still it's much easier to look at the numbers in binary). And I believe my solution is pretty solid.

+ Type matters in this challange. My algorithm worked well for some tests but other tests kept failing
and it took me hours to figure out that the tests expected Integer while my solution returned Long.

+ I try to use tail recursion but Python and Ruby don't optimize for tail recursion.

#### Solution explain:

+ In order to decrease a number, out of the 3 operations (`add, substract and divide`), `divide` is the
fastest (in term of number of operations). So we use `divide` as much as possible.

+ `Divide` doesn't work for odd numbers. So we need an operation the make odd numbers become even. Because we want to
decrease numbers, `substract` seems a better choice than add.

+ However, `substract` is not **always** better. It's worse when it results in an even number that when divided, becomes odd.
In that case, `add` is better. So we need to check 1 step ahead the number resulting from the current number that is going to be divided.

#### Pseudo code
```
def find_steps_count(num, cur_count = 0)
  cur_count += if num == 3
    2
  elsif num == 2
    1
  elsif num == 1
    0
  end

  if num.even?
    cur_count + find_steps_count(num / 2, cur_count)
  else
    bin = num.to_bin
    if second_last_digit_is_one?(bin)
      cur_count + find_steps_count(num + 1, cur_count)
    else
      cur_count + find_steps_count(num - 1, cur_count)
    end
  end
end
```
