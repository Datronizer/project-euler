"""The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 +...+ 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 +...+ 10)^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

""" We can shorten this a crap ton
Recall Binomial theorem
Reference: https://planetmath.org/squareofsum

Basically: The square of a sum is equal to the sum of the squares of all the summands plus the sum of all the double products of the summands in twos.
And since one of the terms is in fact the sum of the squares of all the summands, we can get rid of it prematurely
and instead just find the sum of the double products of the summands in twos.

This is basically multiplying ab, bc, ca for some (a + b + c)^2
The trick here is to multiply without repetition.
"""
num = 100

# Initialize 2 lists
list_a = [int(x) for x in range(1, num + 1)]
list_b = list_a[::-1]

# print(list_a, list_b)

# Now initialize a placeholder variable:
bigsum = 0

# Now we do a funny:
for a in list_a:
    for b in list_b:
        bigsum += a * b
    list_b.remove(a)

for i in range(1, num + 1):
    bigsum -= i**2

print(bigsum * 2)
