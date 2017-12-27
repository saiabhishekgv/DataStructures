'''
link : https://leetcode.com/problems/roman-to-integer/description/

Question 13. Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

'''

'''
References :
1. 
2. 
'''
'''
Solution:
    1. Brute Force :
        - Time Complexity : O(n)
        - Space Complexity : O(1)
        - Run Time : 159ms
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicti = { 'I':1 , 'V':5 , 'X':10, 'L':50 , 'C':100,'D':500, 'M':1000 }
        sum_value = dicti[s[-1]]
        for i in xrange(len(s)-2,-1,-1) :
            if (dicti[s[i]] < dicti[s[i + 1]]) :
                sum_value -= dicti[s[i]];
            else:
                sum_value += dicti[s[i]];

        return sum_value