'''

Question 32 : Longest Valid Parenthesis

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

'''

'''
Resources : 
    1. https://leetcode.com/problems/longest-valid-parentheses/solution/
    2. https://leetcode.com/problems/longest-valid-parentheses/discuss/
'''

'''
Solutions : 
    1. Brute Force : 
        - Time Complexity :O(n^3)
    2. Two scans : 
        - Time Complexity : O(n)
        - Space Complexity : O(1)
'''


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_para = 0
        right_para = 0
        output = 0
        l = len(s)

        for i in range(l):
            if s[i] == '(':
                left_para += 1
            else:
                right_para += 1
            if left_para == right_para:
                output = max(output, 2 * left_para)
            elif right_para >= left_para:
                left_para = right_para = 0

        left_para = right_para = 0

        for i in range(l - 1, -1, -1):
            if s[i] == ')':
                right_para += 1
            else:
                left_para += 1
            if left_para == right_para:
                output = max(output, 2 * right_para)
            elif left_para >= right_para:
                left_para = right_para = 0

        return output


