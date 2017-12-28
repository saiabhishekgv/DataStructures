'''
Link : https://leetcode.com/problems/3sum-closest/description/

Question 16. 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

'''
Resources : 
    1. https://leetcode.com/problems/3sum-closest/discuss/7871
    2.
'''

'''
Solution :
    1. Brute Force :
        - Time Complexity - O(n^3)
        - Space Complexity - O(1)
        - Run Time - TLE
    2. Array with two pointers : 
        - Time Complexity - O(n^2)
        - Space Complexity - O(1)
        - Run Time - 139 ms
'''


class Solution(object):
    def threeSumClosest(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(num) < 3:
            return 0
        num.sort()
        result = s = num[0] + num[1] + num[-1]

        for i in range(len(num) - 2):
            j, k = i + 1, len(num) - 1
            while j < k:
                s = num[i] + num[j] + num[k]
                if s == target:
                    return s
                if abs(s - target) < abs(result - target):
                    result = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1

        return result