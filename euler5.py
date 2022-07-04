"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

# Unfortunately for you, I'm a dumbass, so I'm brute forcing this
# Step 1: Make a function that loop-checks for all divisions from 1 to 20:
# Step 2: keep counting
# Since we're brute-forcing, I recommend checking 1mil numbers at a time

### Go down for the better algorithm
# found = False
# end = 20
# def divisible(num):
#     global found
#     #print("Checking for {}".format(num))
#     for i in range(1, end+1):
#         if num % i != 0:
#             break
#         elif i == end and num % i == 0:
#             print("Found! Number is {}".format(num))
#             found = True
#             break
#
# a = 1
# while found == False:
#     divisible(a)
#     a += 1

# The number is 232,792,560 so if the code isn't responding, give it some time

"""This is a way better way to solve this problem:
Using prime factors, we can deduce the solution by hand without needing codes.
Assume the number we need to guess to be k.
k = 2 = 2
k = 3 = 3
k = 4 = 2 * 2
...
k = 12 = 3 * 4
But since 4 = 2 * 2 so 12 = 2 * 2 * 3.

This is the pattern. Since 4|12 and 2|4 then 2|12 automatically.

Now assume the k = 2520
If k = 2520 then k = 252 * 10 = 28 * 9 * 10 = 4 * 7 * 9 * 10
Well, following the previous logic:
k = 4 * 7 * 9 * 10 = 2 * 2 * 2 * 3 * 3 * 5 * 7

We could also do this:
Multiply each number from 1 to 10 for 2520. Simplify anything that's not prime:
1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
1 * 2 * 3 * 2 * 5 * 1 * 7 * 2 * 3 * 1 = 2520

So I'm going to do something really stupid based on this revelation down below:
"""

# Populate list
maxNumber = 20
primes = []
isPrime = True
list = [int(a) for a in range(2, maxNumber + 1)] # Initialize list
for a in list:
    for b in range(2, a):
        if a % b == 0 and a != b:
            isPrime = False
            break
        else:
            isPrime = True
    if isPrime == False:
        pass
    else:
        primes.append(a)

# Scroll through list
k = 0
j = 0
highestPower = 4 # Based on the highest power of 2 less than maxNumber
while j < highestPower:
    for i in range(len(list)):
        for k in range(len(primes)):
            if list[i] % primes[k] == 0 and list[i] != primes[k]:
                list[i] = round(list[i] / primes[k])
    j += 1

# Clean list up and remove extras
list.sort()
highest = [] # list of highest powers based on primes
for i in primes:
    a = 1
    while i**a < maxNumber:
        a += 1
    highest.append(a-1) # to account for mis-indexing

for i in range(len(highest)):
    while list.count(primes[i]) > highest[i]:
        # print("For the index {}, I found {} count(s) compared to the expected {}".format(i, list.count(primes[i]), highest[i]))
        list.remove(primes[i])

result = 1
for i in list:
    result *= i
print(result)
