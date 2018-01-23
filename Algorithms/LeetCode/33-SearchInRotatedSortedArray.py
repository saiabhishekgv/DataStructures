'''
Question 33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
'''
'''
Resources :
    1. https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/
    2.
'''

'''
Solution :
    1.Linear Search : 
        - Time Complexity : O(n) 
    2. Binary Search : 
        - Time Complexity : O(log n)
        -Run Tieme : 40 ms
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1
        elif len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                if (target >= nums[low] and target < nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target >= nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1 if nums[low] != target else low
