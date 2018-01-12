'''

Question 26. Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''

'''
References : 
    1. https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/
    2. https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/11757
'''
'''
Solution : 
    1. Two pointers and Array : 
        - Time Complexity : O(n)
        - Run Time : 87 ms
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        if l < 2:
            return l

        prev = nums[0]
        length = 1
        n = 0

        for i in xrange(1, l):
            n += 1
            if nums[i] == prev:
                continue
            else:
                prev = nums[n]
                nums[length], nums[n] = nums[n], nums[length]
                length += 1

        return length
