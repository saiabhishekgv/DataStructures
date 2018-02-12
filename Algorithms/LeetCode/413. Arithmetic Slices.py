'''

413. Arithmetic Slices
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

'''
'''
References : 
    1. https://leetcode.com/problems/arithmetic-slices/solution/
    2. https://leetcode.com/problems/arithmetic-slices/discuss/90058/Simple-Java-solution-9-lines-2ms
'''
'''
Solution : 
    Refer to references.
    1. Brute Force : O(n^3)
    2. Optimized Brute Force : O(n^2)
    3. Recursion : O(n), O(n)
    4. Dynamic programming : O(n), O(n)
    5. Optimized dp : O(n), O(1)
    6. Math Forumla : O(n)
'''


class Solution:
    def numberOfArithmeticSlices_6(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        sumValue = 0
        l = len(A)
        for i in range(2, l):
            if (A[i] - A[i - 1]) == (A[i - 1] - A[i - 2]):
                count += 1
            else:
                sumValue += ((count + 1) * count) / 2
                count = 0

        sumValue += count * (count + 1) / 2

        return int(sumValue)

    def numberOfArithmeticSlices_5(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = 0
        sumValue = 0
        l = len(A)
        for i in range(2, l):
            if (A[i] - A[i - 1]) == (A[i - 1] - A[i - 2]):
                dp += 1
                sumValue += dp
            else:
                dp = 0

        return sumValue