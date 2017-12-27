'''
coding : utf - 8
Link : https://leetcode.com/problems/3sum/description/
Question 15. 3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
'''
Resources : 
1.
2.
'''

'''
Solution :
    1. Brute Force :
        - Time Complexity : O(n^3)
        - Space Complexity : O(1)
        - Run Time : TLE
    2. Array with two pointers : 
        - Time Complexity : O(n^2)
        - Space Complexity : O(1)
        - Run Time : 1236 ms
'''


class Solution(object):
    def threeSum_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        result = []
        prev_target = sys.maxint
        for index, i in enumerate(nums):
            target = -i
            if prev_target == i:
                continue
            remaining = self.twoSum_1(nums[index + 1:], target)
            for k in remaining:
                result.append([i] + k)
            prev_target = i
        return result

    def twoSum_1(self, new_nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(new_nums) < 2:
            return []

        last_occured = {}
        output = []
        last_1 = sys.maxint
        last_2 = sys.maxint
        for index, num in enumerate(new_nums):
            other_number = target - num
            if (other_number in last_occured) and last_1 != other_number and last_2 != num:
                output.append([other_number, num])
                last_1 = other_number
                last_2 = num
                last_occured[num] = index
            else:
                last_occured[num] = index

        return output

    def threeSum_2(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res