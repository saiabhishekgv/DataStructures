'''
Question 718. Maximum Length of Repeated Subarray

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

'''

'''
References : 
    1.
    2.
'''

'''
Solution : 
    1. Brute Force : 
        - Time Complexity : O( m * n * min(m,n) )
        - Space Complexity : O(n)   
    2. Binary Search with Naive Check :
        - Time Complexity :  O((M + N) * min(M, N) * log((min(M, N))))
        - Space Complexity : O(n)
    3. 
'''

import collections

class Solution(object):
    def findLength1(self, A, B):
        ans = 0
        Bstarts = collections.defaultdict(list)
        for j, y in enumerate(B):
            Bstarts[y].append(j)

        for i, x in enumerate(A):
            for j in Bstarts[x]:
                k = 0
                while i+k < len(A) and j+k < len(B) and A[i+k] == B[j+k]:
                    k += 1
                ans = max(ans, k)
        return ans

    def findLength3(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        print memo
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
                    print A[i]

            for row in memo:
                for col in row :
                    print col, ' ',
                print ''
            print '====='

        return max(max(row) for row in memo)

a = Solution()
print a.findLength3([1,2,3,1,5],[3,1,2,3,1])