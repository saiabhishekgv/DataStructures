'''
Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

'''
References : 
    1.https://leetcode.com/problems/palindrome-number/solution/ 
'''
'''
Solution :
1. Reverse half of digits : 
    - Time Complexity : 
    - Runtime: 359 ms
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_number = 0
        while x > reversed_number:
            reversed_number = reversed_number * 10 + (x % 10)
            x = x / 10

        return x == reversed_number or x == reversed_number / 10

