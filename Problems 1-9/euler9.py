"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
This looks like another case of binomial theorem.
We have:
a^2 + b^2 = c^2
a + b + c = 1000

Isolate a and b to get:
a^2 + b^2 = c^2
a   + b   = 1000 - c

Then:
a^2 + b^2 + 2ab = c^2 + 2ab
a^2 + b^2 + 2ab = (1000 - c)^2

Thus
> c^2 + 2ab = 1000^2 - 2000c + c^2
> 2ab = 1000000 - 2000c
> ab = 500000 - 1000c

If c is 500 then ab = 0 and thus either of which will be 0 which isn't a natural number
If c > 500 then ab is negative.
Thus c must be < 500 and a < b < c < 500
But if c < 500 and a + b + c = 1000 then a + b > 500
