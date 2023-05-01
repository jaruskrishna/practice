from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print("The list is - \n", list(nums))
        print("The target is - \n", target)
        print("-------------------\n")
        elements = dict()

        for index, value in enumerate(nums):
            ans = target - value
            # ans = the one we are searching
            # we are keeping all the elements on dict called elements to check whether we have seen the ans value before by using dic

            if ans in elements:
                print(elements[ans], index)
                return [elements[ans], index]

            # adding current value to dic if ans is not in the elements we have seen before
            elements[value] = index

        # we are returning empty list
        return []

if __name__ == '__main__':
    print("Hello to TwoSum.\n")
    l = [3,2,4] #list(input("Enter the list -\n"))
    t = 6 #int(input("Enter the Target as well - "))
    a = Solution()
    a.twoSum(l, t)


#  https://leetcode.com/problems/two-sum/discuss/2623088/Python-Easiest-Solution-Explained-or-90-Faster