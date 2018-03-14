'''
Question 500. Keyboard Row

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

'''

'''
Resources : 
    1. https://leetcode.com/problems/keyboard-row/discuss/97888/one-liner-Ruby-+-Python
    2. 
'''
'''
Solution : 
    1. Regex :
        - Time complexity : O(N) N->length of string
'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        import re
        res = []
        for word in words:
            s = re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match(word)
            if s is not None:
                res.append(word)
            # [word for word in words if re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match(word)]

        return res

    def findWords_2(self,words):
        import re
        return [word for word in words if re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)').match(word)]
