"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

# Unfortunately for you, I'm a mathematician, so I'm brute forcing this
# Step 1: Make a function that loop-checks for all divisions from 1 to 20:
# Step 2: keep counting
# Since we're brute-forcing, I recommend checking 1mil numbers at a time

found = False
end = 20
def divisible(num):
    global found
    #print("Checking for {}".format(num))
    for i in range(1, end+1):
        if num % i != 0:
            break
        elif i == end and num % i == 0:
            print("Found! Number is {}".format(num))
            found = True
            break

a = 1
while found == False:
    divisible(a)
    a += 1

# The number is 232,792,560 so if the code isn't responding, give it some time
