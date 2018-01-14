'''

Question 29. Divide Two Integers

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

'''

'''
References : 
    1. https://leetcode.com/problems/divide-two-integers/discuss/13407
'''

'''
Solution : 
    1. Bit Manipulation :
        - Time Complexity : 
        - Run Time : 62 ms
'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0

        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res

        return min(max(-2147483648, res), 2147483647)


