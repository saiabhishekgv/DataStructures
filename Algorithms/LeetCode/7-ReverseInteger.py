'''

Question 7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

''' 
Resources : 
    1. 

'''

'''
Solution :
    1. Brute Force :
        - Time Complexity - O(n)
        - Run Time : 48 ms 
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # if number is between -9 to +9, reversing will yield same value
        if abs(x) < 10:
            return x

        # save the sign
        sign = 1 if x >= 0 else -1
        # make x positive. If it is negative, muliplying with -1 will give positive.
        x = sign * x

        # make number a string
        x = str(x)

        # reverse the string
        x = x[::-1]

        # convert the number into  integer and multiply with sign
        x = sign * int(x)

        # return x if the integer is not overflow else return 0.
        return 0 if x >= 2147483647 or x <= (-2147483647 - 1) else x