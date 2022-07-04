'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

# A number can often be broken down into prime factors, aka factors that are prime.
# 13195 = 5 * 7 * 13 * 29.
# What we can do is to loop the number through an if-check and divide until it's

number = 600851475143
list = []

a = 1
while a <= number:
    if number % a == 0:
        list.append(a)
        number /= a
        a += 1
    else:
        a += 1

print(list)
print(list[-1])
