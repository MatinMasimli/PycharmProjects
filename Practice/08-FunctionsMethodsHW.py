#08-Functions and Methods Homework

from math import pi
from math import pow
import string

def vol(rad):
    return (4 * pi * pow(rad, 3))/3

def ran_check(num,low,high):
    return num > low and num < high

def up_low(s):
    upp = 0
    low = 0
    for ch in s:
        if ch.isupper():
           upp += 1
        elif ch.islower():
           low += 1
    print(str(upp) + " : " + str(low))

def unique_list(lst):
    outList = []
    for num in lst:
        if num not in outList:
            outList.append(num)
    return outList

def multiply(numbers):
    result = 1

    for num in numbers:
        result = result * num
    return result

def palindrome(s):
    beginInd = 0
    endInd = len(s) - 1
    count = 0

    while beginInd <= endInd:
        if s[beginInd] == s[endInd]:
            beginInd += 1
            endInd -= 1
            count += 1
        else:
            return False

    if count == beginInd:
        return True

def ispangram(str1, alphabet=string.ascii_lowercase):

    allCharLen = len(alphabet)
    count = 0

    for ch in alphabet:
        if ch in str1:
            count += 1

    return allCharLen == count


def main():
    print(vol(2))
    ran_check(5, 2, 7)
    s = 'What is your name?'
    up_low(s)
    print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
    print(multiply([1, 2, 3, -4]))
    print(palindrome('helabacleh'))
    print(ispangram("The quick brown fox jumps over the lazy dog"))


if __name__ == "__main__":
    main()