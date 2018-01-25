'''

Question 38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

'''

'''
Resources : 
    1. https://leetcode.com/problems/count-and-say/discuss/15999 
    2.
'''

'''
Solution : 
1. Brute Force : 
    - Time Complexity : O(n^3)
2. Revised Brute Force :
    - Time Complexity : O(n^2)
    - Run Time : 40 ms
'''



class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 2:
            return '1'

        res = '11'

        while n > 2:
            output = ''
            i = 0
            while i < len(res):
                j = i

                while j < len(res):
                    if res[j] != res[i]:
                        break
                    j += 1

                output += str(j - i) + res[i]
                i = max(j, i + 1)

            n = n - 1
            res = output

        return res

    def countAndSay_2(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 2:
            return '1'

        res = '11'

        while n > 2:

            output = ''
            count = 0

            l = len(res)

            for i in xrange(l):
                count += 1
                if i + 1 < l and res[i] == res[i + 1]:
                    continue
                else:
                    output += str(count) + res[i]
                    count = 0

            n = n - 1
            res = output

        return res