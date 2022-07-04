"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

# Step 1: Initialize a list of all numbers that are multiples of 3 or 5
# There are 2 ways (I could think of) that you can do:
# 1. Initialize all 1000 numbers and mod 3 and 5. If mod = 0, we keep.
# 2. Multiply 3 until you hit 1000, same with 5.

# I went with Method 1

multiples = []

for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)

# Step 2: Sum it all up
print(sum(multiples))
