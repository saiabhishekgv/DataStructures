'''

Question 35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 1:

Input: [1,3,5,6], 0
Output: 0

'''

'''
Resources :
    1. https://leetcode.com/problems/search-insert-position/discuss/ 
    2. https://leetcode.com/problems/search-insert-position/discuss/
'''

'''
Solution :
    1. Linear Search:
        - Time Complexity : O(n)
    2. Binary Search :
        - Time Complexity : O( log n)
        - Run time : 36 ms
'''


class Solution(object):
    def searchInsert(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(num) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if mid == 0 and num[mid] > target:
                return mid
            elif mid == len(num) - 1 and num[mid] < target:
                return mid + 1
            elif num[mid] == target:
                return mid
            elif num[mid] > target and num[mid - 1] < target:
                return mid
            elif num[mid] < target and num[mid + 1] > target:
                return mid + 1
            elif num[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return low