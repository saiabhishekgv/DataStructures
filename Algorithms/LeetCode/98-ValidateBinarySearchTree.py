'''

Question 98. Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''

'''
Resources :
    1. https://leetcode.com/problems/validate-binary-search-tree/discuss/32112
    2. https://leetcode.com/problems/validate-binary-search-tree/discuss/32112
'''


'''
Solution : 
    1. Recursion : 
        - Time Complexity : O(n)
        - Run Time : 89ms
    2. Stack :
        - Time Complexity : O(n)
'''

import sys


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isValid(root, sys.maxint, -sys.maxint - 1)

    def isValid(self, root, max_value, min_value):
        if root is None:
            return True
        if root.val >= max_value or root.val <= min_value:
            return False
        return self.isValid(root.left, root.val, min_value) and self.isValid(root.right, max_value, root.val)