'''

Question 104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

'''
'''
Resources : 
    1. https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/34212
    2. 
'''
'''
Solution : 
    1. Recursive : 
        - Time Complexity : O(n)
        - run time : 55ms
    2.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None :
            return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))