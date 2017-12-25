'''

Question 3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Solution :
    1. Using HashMap
        Time Complexity - O(n^2)
        Runtime - 772 ms

    2. Using HashMap using sliding Window
        Time Complexity - O(n)
        Runtime - 112 ms
'''


class Solution(object):
    def lengthOfLongestSubstring_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        get_count = {}
        counter = 0
        max_length = 0

        for index, i in enumerate(s):
            get_count[i] = 1
            current_length = 1
            for j in xrange(index + 1, len(s)):
                if s[j] in get_count:
                    break
                else:
                    get_count[s[j]] = 1
                    current_length += 1
            max_length = max_length if max_length > current_length else current_length
            get_count.clear()

        return max_length

    def lengthOfLongestSubstring_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        get_count = {}
        ans = 0
        i = 0

        for j in xrange(len(s)):
            if s[j] in get_count:
                i = max(get_count[s[j]], i)
            ans = max(ans, j - i + 1)
            get_count[s[j]] = j + 1

        return ans
