'''

Question 8. String to Integer (atoi)
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.
If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument,
please click the reload button  to reset your code definition.

'''

'''
Resources : 
    1. https://discuss.leetcode.com/topic/115019/python-beats-65-solution
    2. https://discuss.leetcode.com/topic/2666/my-simple-solution    
'''

'''
Solution :
    1. Brute Force : 
        - Time Complexity : O(n)
        - Runtime: 66 ms
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        ans = 0
        number_started = False
        sign = 1
        signflag = False

        for i in str:
            if i == ' ':
                if number_started == False:
                    continue
                else:
                    break
            if (i == '-' or i == '+') and number_started == False and signflag == False:
                sign = -1 if i == '-' else 1
                signflag = True
                number_started = True
            elif ord(i) >= 48 and ord(i) <= 57:
                number_started = True
                ans = (ans * 10) + (ord(i) - ord('0'))
            else:
                break

        if ans >= 2 ** 31:
            ans = 2 ** 31
            if sign == 1:
                return ans - 1
            else:
                return sign * ans

        return sign * ans

