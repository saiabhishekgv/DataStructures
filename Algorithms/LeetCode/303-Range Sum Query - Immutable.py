'''

Question 303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:
    You may assume that the array does not change.
    There are many calls to sumRange function.

'''

'''
Resources : 
    1. https://leetcode.com/problems/range-sum-query-immutable/solution/
    2. https://leetcode.com/problems/range-sum-query-immutable/discuss/75192/Java-simple-O(n)-init-and-O(1)-query-solution
'''

'''
Solution :
    1. Brute Force :
        - Time complexity : O(n)
        - Space complexity : O(1)
    2. Caching :
        - Time complexity : O(1)
        - Space complexity : O(n)
'''


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) == 0:
            return
        self.nums = [nums[0]]
        for i in range(1, len(nums)):
            self.nums.append(self.nums[i - 1] + nums[i])

        print(self.nums)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[j] - (self.nums[i - 1] if i > 0 else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)