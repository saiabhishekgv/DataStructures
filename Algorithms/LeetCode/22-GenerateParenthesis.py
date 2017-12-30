'''

Link : https://leetcode.com/problems/generate-parentheses/description/

Question 22. Generate Parenthesis

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''

'''
Resources : 

'''
'''
Solution : 
    1. Brute Force : 
        - Time Complexity : O(2^n)
        - Space Complexity : O(1)
        - Run Time : TLE
    2. Backtrack : 
        - Time Complexity : O( 4^n/(sqrt(n))
        - Space Complexity : O(1)
        - Run Time : 45ms        
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        par = ['(', ')']
        temp_ans = []
        self.get_pair(n, temp_ans, ans, 0, 0)
        return ans

    def get_pair(self, n, temp_ans, ans, left, right):

        if len(temp_ans) == (n * 2):
            ans.append(''.join(temp_ans))
            return ans

        if right > left:
            return ans

        if left < n:
            temp_ans.append('(')
            self.get_pair(n, temp_ans, ans, left + 1, right)
            temp_ans.pop()

        if right < n:
            temp_ans.append(')')
            self.get_pair(n, temp_ans, ans, left, right + 1)
            temp_ans.pop()

        return ans

