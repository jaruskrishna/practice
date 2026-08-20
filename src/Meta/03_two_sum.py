# Interview question:
# Given an array of integers and a target, return the indices of two numbers that add up to the target.
#
# Hint:
# Store each number's index in a dictionary while looking for target - current_number.
# [0, -1, 2, -3, 1], target = -2

def twosum (nums, target):

    n = len(nums)

    for i in range(n):

        for j in range(i +1, n):
            if nums[i] + nums[j] == target:
                print("The 2 numbers are ", nums[i], " & ", nums[j] )

if __name__ == '__main__':
    print("====== HELLO TWO SUM ======")
    nums = [1,1,2,3,3,4]
    taregt = 5
    twosum(nums, taregt)
    print("The 2 numbers are ",  )


