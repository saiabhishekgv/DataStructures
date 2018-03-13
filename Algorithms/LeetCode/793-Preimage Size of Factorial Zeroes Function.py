'''

Question 793. Preimage Size of Factorial Zeroes Function

Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end. Given K, find how many non-negative integers x have the property that f(x) = K.

Example 1:
Input: K = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

Example 2:
Input: K = 5
Output: 0
Explanation: There is no x such that x! ends in K = 5 zeroes.
Note:

K will be an integer in the range [0, 10^9].

'''

'''
Resources : 
    1. https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/solution/
    2.
'''

'''
Solution : 
    1. Brute Force : 
        - Time complexity : O(2*k-1)
        - Runtime : TLE 
    2. Binary Search : 
        - Time Complexity : O (log^2 K)
        - Space complexity : O( log K)
'''


class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        low = K
        high = 5 * K + 1
        count = 0

        def get_zeros(mid):
            if mid == 0:
                return 0
            return mid / 5 + get_zeros(mid / 5)

        while low < high:
            mid = int(low + (high - low) / 2)
            z = get_zeros(mid)
            if z == K:
                return 5
            elif z < K:
                low = mid + 1
            else:
                high = mid - 1

        return 0

