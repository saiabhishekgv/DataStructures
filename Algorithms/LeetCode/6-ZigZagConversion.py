'''
Question 6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like
this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

'''
Resources : 
    1. https://discuss.leetcode.com/topic/22925/if-you-are-confused-with-zigzag-pattern-come-and-see
    2. https://discuss.leetcode.com/topic/34573/python-o-n-solution-in-96ms-99-43
'''

'''
Solution : 
    1. Brute Force : 
        - Time Complexity : O(n) 
        - Run Time : 105 ms
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows >= len(s) or numRows == 1:
            return s

        L = [''] * numRows
        index = 0
        step = 1  # direction to move

        for x in s:
            L[index] += x
            # index at beginning move forward
            if index == 0:
                step = 1
            # index at end move backward

            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)