# Interview question:
# Given an integer array, return whether any value appears at least twice.
#
# Hint:
# A set can tell you if a number has already been seen.

def dup(nums):
    seen = set()
    duplicate = set()

    for num in nums:
        if num in seen:
            duplicate.add(num)
        else:
            seen.add(num)
    print("The duplicates are - ", duplicate)


if __name__ =='__main__':
    print("=== Find all duplicates in a list=====")
    nums = [1,1,2,2,3,3,4,5,6,7,]
    result = dup(nums)
    #print("Duplicates are - ", nums)