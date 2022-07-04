"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


"""The best way I could think of is to break it down into components.
This palindrome probably has the pattern abccba where:
abccba = 100000a + 10000b + 1000c + 100c + 10b + 1a

We must achieve abccba from two 3-digit numbers, def and ghi where:
> (100d + 10e + 1f) * (100g + 10h + 1i) = abccba
> 10000dg + 1000dh + 100di + 1000eg + 100eh + 10ei + 100fg + 10fh + 1fi
> 10000dg + 1000(dh + eg) + 100(di + eh + fg) + 10(ei + fh) + 1fi
(UNFINISHED TRAIN OF THOUGHT HERE)"""

palindromes = []

def palindrometest(num):
    global palindromes
    isPalindrome = True
    checklist = [int(a) for a in str(num)]
    for i in range(len(checklist)):
        if checklist[i] != checklist[-(i+1)]:
            isPalindrome = False
            break
    if isPalindrome:
        palindromes.append(num)

list = []
for i in range(100, 1000):
    for j in range(100, 1000):
        list.append(i * j)
list.sort()

for i in list:
    palindrometest(i)

print(palindromes)
print(max(palindromes))
