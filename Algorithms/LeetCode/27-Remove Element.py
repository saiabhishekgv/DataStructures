'''

Question 27. Remove Element

Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

'''

'''
References : 
    1.https://leetcode.com/problems/remove-element/solution/
    2.https://leetcode.com/problems/remove-element/discuss/12289
'''

'''
Solution : 
    1. Two Pointers
        - Time Complexity : O(n)
        - Run Time : 48 ms
'''


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        if last + 1 == 0:
            return 0
        while first < last and first < len(nums):
            if nums[first] == val:
                if nums[last] != val:
                    nums[first], nums[last] = nums[last], nums[first]
                else:
                    last -= 1
            else:
                first += 1

        for i in range(first, len(nums)):
            if nums[i] != val:
                first += 1
            else:
                break

        return first

