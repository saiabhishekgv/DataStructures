'''

Question 5 : Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

'''

'''

References : 

1. https://leetcode.com/problems/longest-palindromic-substring/solution/
2. https://articles.leetcode.com/longest-palindromic-substring-part-ii/
3. https://www.felix021.com/blog/read.php?2040
4. https://en.wikipedia.org/wiki/Longest_palindromic_substring
5. https://johanjeuring.blogspot.com/2007/08/finding-palindromes.html
6. https://www.akalin.com/longest-palindrome-linear-time
'''

'''
Solution : 
    1. Brute Force :
        - Time Complexity : O(n^3)
        - Run Time : TLE 
'''


class Solution(object):
    def longestPalindrome_1(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = len(s)
        if l == 0:
            return 0

        max_length = 1
        result = s[0]
        for i in xrange(l - 1):
            for j in xrange(i + 1, l):
                if self.isPalindrome_1(s, i, j):
                    if max_length < (j - i + 1):
                        max_length = j - i + 1
                        result = s[i:j + 1]

        return result

    def isPalindrome_1(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return 0
            i += 1
            j -= 1
        return 1