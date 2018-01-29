'''
Question 110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

'''
'''
Resources : 
    1. https://leetcode.com/problems/balanced-binary-tree/discuss/35708
    2.
'''

'''
Solution: 
    1. Recursion :
        - Time Complexity : O(n)
        - Run time : 97 ms
    2.
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(
            self.height(root.left) - self.height(root.right)) <= 1

    def height(self, root):
        if root is None:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        return 1 + max(l, r)
