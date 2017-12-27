'''
coding: utf-8

Question 10. Regular Expression Matching

Implement regular expression matching with support for "." and "*".

"." Matches any single character.
"*" Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

'''

'''
Resources : 
1. 
2. 
'''
'''
Solution : 
    1. Brute Force : 
       - Time Complexity : O((T+P)2^(T+(P/2)) 
       - Space Complexity : O((T+P)2^(T+(P/2))
       - Run Time : TLE 
    
    2. Dynamic Programming : 
'''


class Solution(object):
    def isMatch_1(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])