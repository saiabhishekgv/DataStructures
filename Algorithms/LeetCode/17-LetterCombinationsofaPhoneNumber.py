'''

Link : https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Question 17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

2 - abc, 3-def, 4- ghi, 5-jkl, 6-mno, 7-pqrs, 8-tuv, 9-wxyz

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''


'''
Solution:
1. Backtrack : 
    - Time Complexity : O(n^2)
    - Run Time : 35ms
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        ans = []
        l = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        if ('#' in digits) or ('1' in digits) or ('*' in digits):
            return ans
        ans = self.get_combinations(digits, l, ans, [], 0)
        return ans

    def get_combinations(self, digits, l, ans, temp_ans, index):
        if len(temp_ans) == 0 and len(digits) == 0:
            return ans
        elif len(digits) == index and len(temp_ans) == len(digits):
            ans.append(''.join(temp_ans))
            return ans
        for i in xrange(index, len(digits)):
            string = l[int(digits[i])]
            for j in string:
                temp_ans.append(j)
                ans = self.get_combinations(digits, l, ans, temp_ans, i + 1)
                temp_ans.pop()
        return ans