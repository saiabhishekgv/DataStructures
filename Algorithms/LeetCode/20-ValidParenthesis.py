'''

Link : https://leetcode.com/problems/valid-parentheses/description/

Question 20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

'''
Resources : 
    1. https://leetcode.com/problems/valid-parentheses/discuss/9203
    2. 
'''

'''
Solution : 
    1. Brute Force : 
        - Time Complexity : O(n^2)
        - Space Complexity : O(1)
        - Run Time : TLE
    2. Stack :
        - Time Complexity : O(n)
        - Space Complexity : O(1)
        - Run Time : 35 ms
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        o = ['[','(','{']
        stack = []
        for index,i in enumerate(s) :
            if i in o:
                stack.append(i)
            elif len(stack)>0:
                if i == ']' and stack[-1] != '[' :
                    return False
                elif i == ')' and index>0 and stack[-1] != '(':
                    return False
                elif i == '}' and index>0 and stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            else:
                return False
        if len(stack) > 0 :
            return False
        else:
            return True