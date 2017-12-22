'''

LeetCode Question - 1 : https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


'''
Solution 1 : (defined in twoSum_1 method)
    Time O(n^2) --> Brute Force Solution
    Runtime: 5245 ms
    
Solution 2 : (defined in twoSum_2 method)
    Time O(n) --> Using Dictionary
    Runtime: 35 ms
'''


class Solution(object):
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for first_num in xrange(len(nums)-1):
            for second_num in xrange(first_num + 1, len(nums)):
                if nums[first_num] + nums[second_num] == target:
                    return [first_num, second_num]
        return []

    def twoSum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        last_occured = {}
        for index, num in enumerate(nums):
            other_number = target - num
            if other_number in last_occured:
                return [last_occured[other_number], index]
            else:
                last_occured[num] = index
        return []

