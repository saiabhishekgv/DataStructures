'''

Question 34. Search For a Range

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

'''
'''
Resources : 
    1.https://leetcode.com/problems/search-for-a-range/solution/ 
    2.
'''
'''
Solution :
    1. Linear Search : 
        - Time Complexity : O(n)
    2. Binary Search :
        - Time Complexity : O(log n)
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums) - 1
        left = -1
        right = -1
        l = len(nums)

        while low <= high:
            mid = low + (high - low) / 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    left = mid
                    break
                else:
                    high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if left == -1:
            return [left, right]

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if nums[mid] == target:
                if mid + 1 == l or nums[mid + 1] != target:
                    right = mid
                    break
                else:
                    low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return [left, right]