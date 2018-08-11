# google-foobar
This repo is an archive for my solutions for Google Foobar challenges, and also how I approached to them in a dairy-like fashion.

This repo can also be useful for others as a reference to learn or compare each other's solutions. I usually do this but only **after I submitted** the solution.

## Tips

### A flaw in Foobar

I found a flaw in Foobar which when exploited, can possibly reveal inputs of all test cases. This flaw is likely known and may be intentional because some edge test cases are amazingly too hard to solve (at least to me) without knowing the exact inputs, so Foobar probably provides this flaw as a hidden tool to help solve the challenges.

In a level-2 challenge, I was so desperate to know the inputs of one edge case (test case 10), that I found this flaw. I exploited this flaw, which then helped me solve the edge case instantly.

Although it's a great help sometimes, it alone cannot solve the challenges and a proper algorithm is still needed. I reported this to Foobar but no response yet so it's probably better not to describe the flaw here.

### A bug in Foobar

I found a bug in Foobar that **global variables are shared across test cases**. Global variables are usually discouraged but in my defense, I'm not an advanced Python user and I just wanted to avoid passing around the arguments.

I found this bug when doing level-4 challenge. It was a huge pain because no matter how much I was confident in my solution, my solution kept failing at test 10. After a massive amount of retries and by exploiting the flaw above, I knew the correct output and I also knew my solution returned the correct output in my localhost but somehow returned a weird value in Foobar sandbox. I even suspected that FooBar sandbox used less precision in `math.atan2` intentionally to trick challengers (I then confirmed it doesn't), or that the hashing algorithm in `dict()` in FooBar sandbox was broken, so it had collisions. Then, with some luck and lots more retries, I found that global variables are shared across test cases.

I already reported this bug to Foobar but no response yet. I share this bug so that you won't have a painful time like I did.

## Notes
Python is not my main language and I barely knew Python so I usually started with Ruby first for quicker prototype solutions. Ruby codes here are just prototype so please ignore Ruby codes and focus on Python codes only.

My codes are quite verbose to better explain my thinkings and also for self-documented codes (hopefully).

## How did I get to Foobar?
I was trying to use [Google Chart](https://developers.google.com/chart/) so I did a lot of searches about it. Unlike others, I didn't see a big banner from Foobar in Google search results. Instead, on Google pages (both Google Chart pages and Google search results pages), I noticed there was a small Foobar icon (probably 50x50 pixels) at top right corner. So the invitation was not very visible.
