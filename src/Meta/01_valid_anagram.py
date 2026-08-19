# Interview question:
# Given two strings, determine if one string is an anagram of the other.
#
# Hint:
# Compare character frequencies, or sort both strings and compare them.

from collections import Counter

def ana(str1, str2):

    clr_str1 = str1.replace(" ","").lower()
    clr_str2 = str2.replace(" ","").lower()

    if len(clr_str1) != len(clr_str2):
        print("Not an Anagram")

    ctr_str1 = Counter(clr_str1)
    ctr_str2 = Counter(clr_str2)

    print("Countered Str1 - ", ctr_str1)
    print("Countrred Str2 - ", ctr_str1)

    if ctr_str1 == ctr_str2 :
        print("an Anagram")
    else :
        print("Sorry Not an Anagram.")

if __name__ == '__main__':
    a = str(input("Enter First string: "))
    b = str(input("Enter Second string: "))
    ana(a, b)

