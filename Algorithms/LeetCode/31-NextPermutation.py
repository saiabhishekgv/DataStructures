'''

Question 31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 => 1,3,2
3,2,1 => 1,2,3
1,1,5 => 1,5,1

'''

'''
Resources:
    1. https://leetcode.com/problems/next-permutation/discuss/
    2. https://leetcode.com/problems/next-permutation/solution/
'''

'''
Solution : 
    1. Brute Force :
        - Time Complexity : O(n!)
    2. Two Pointers : 
        - Time Complexity : O(n)
        - Run Time : 61 ms 
'''


class Solution(object):
    def nextPermutation(self, nums):

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        print i

        if i <= 0:
            left = 0
            right = len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return

        # Find successor to pivot
        j = len(nums) - 1
        while nums[j] <= nums[i - 1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # Reverse suffix
        nums[i:] = nums[len(nums) - 1: i - 1: -1]

        return