'''
Question 30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

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