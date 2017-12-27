'''
Link :  https://leetcode.com/problems/container-with-most-water/description/

Question 11. Container With Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

'''

''' 

Resources : 
    1. https://leetcode.com/problems/container-with-most-water/solution/
    2. https://leetcode.com/problems/container-with-most-water/discuss/6100
'''

'''
Solution : 
    1. Brute Force : 
        - Time Complexity : O(n^2)
        - Space Complexity : O(1)
        - Run Time : TLE
    2. One Pass with Two pointers : 
        - Time Complexity : O(n)
        - Space Complexity : O(1)
        - Run Time : 85ms  
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        output = 0
        low = 0
        high = len(height) - 1
        while low < high:
            output = max(output, min(height[low], height[high]) * (high - low))

            if height[low] < height[high]:
                low += 1
            else:
                high -= 1

        return output



