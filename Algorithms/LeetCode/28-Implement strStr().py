'''

Question 28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

'''

'''

References : 
    1. https://leetcode.com/problems/implement-strstr/discuss/12814
    2. https://leetcode.com/problems/implement-strstr/discuss/12886

'''

'''
Solution : 
    1. Brute Force :
        - Time Complexity : O(n+m)
        - Run Time : 34 ms 
    2. Regex : 
        - Time Complexity : O(n*m) 
        - Run Time : 163 ms
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        for i in range(len(haystack)):
            if i+len(needle)>len(haystack):
                return -1
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1

    def strStr_2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        import re

        match = re.finditer(needle, haystack)
        indices = [m.start(0) for m in match]

        if len(indices) > 0:
            return indices[0]

        return -1
