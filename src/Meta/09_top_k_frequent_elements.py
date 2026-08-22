# Interview question:
# Given an integer array, return the k most frequent elements.
#
# Hint:
# Count frequencies first, then use a heap, bucket sort, or sorting by count.
# input nums = [1,1,1,2,2,3,3,4,4,5,5,5,5,6] k= 3

from collections import defaultdict
import heapq

def topkfreq(nums, k):
    heap = []
    ddt = defaultdict(int)

    for num in nums:
        ddt[num] += 1
    print("The Default Dict is -- ",ddt)

    for key, val in ddt.items():
        heapq.heappush(heap, (val, key))
        if len(heap) > k:
            heapq.heappop(heap)
    return [i[1] for i in heap]

if __name__ == '__main__':
    print("Top k times occurance in a list ")
    nums = [1,1,1,2,2,3,3,4,4,5,5,5,5,6] 
    k = 3
    results = topkfreq(nums,k)
    print(results)


    # [1,1,1,2,2,3,3,4,4,5,5,5,5,6] k= 3
    # First build this -
    # [[1:3], [2:2], [3:2], [4:2], [5:4], [6:1]]
    #.  k:v