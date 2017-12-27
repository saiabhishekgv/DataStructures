'''
Link : https://leetcode.com/problems/longest-common-prefix/description/

Question 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
'''

'''
Resources : 
    1. https://leetcode.com/problems/longest-common-prefix/solution/  (highly recommended) 
    2. 
'''

'''
Solution :
    1. Horizontal Scanning -> see resources 1
    2. Vertical Scanning -> see resources 1
    3. Divide and Conquer -> see resources 1
    4. Binary Search -> see resources 1
        - Time Complexity :
        - Space Complexity : O(S * log(n)) ==> S, sum of all characters in all strings
        - Run Time :
    5. Trie -> see resources 1
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        min_length = sys.maxint
        for i in strs:
            min_length = min(min_length, len(i))
        low = 0
        high = min_length

        while low <= high:
            mid = (low + high) / 2
            if self.isCommon(strs, mid):
                low = mid + 1
            else:
                high = mid - 1

        first = strs[0]
        return first[:(low + high) / 2]

    def isCommon(self, strs, length):
        first = strs[0]
        prefix = first[:length]
        for i in strs:
            if i[:length] != prefix:
                return False
        return True

