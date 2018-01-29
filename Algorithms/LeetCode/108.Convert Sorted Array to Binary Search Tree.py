'''

Question 108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''

'''
References : 
    1.
    2.
'''

'''
Solution : 
    1. Brute Force with Recursion:
        - Time Complexity : O(n)
        - Rum TIme : 89 ms
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l == 0:
            return None
        elif l == 1:
            return TreeNode(nums[0])

        middle = l / 2
        root = TreeNode(nums[middle])

        leftInts = nums[:middle]
        rightInts = nums[middle + 1:]

        root.left = self.sortedArrayToBST(leftInts)
        root.right = self.sortedArrayToBST(rightInts)

        return root