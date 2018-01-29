'''
Question 173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.
Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

'''
'''
Resources : 
    1. https://leetcode.com/problems/binary-search-tree-iterator/discuss/52526
'''
'''
Solution : 
    1. Using Stacks : 
        - Time Complexity : O(1) and O(h)
        - Runtime : 95 ms 
'''


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushAllNodes(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        lowNode = self.stack.pop()
        self.pushAllNodes(lowNode.right)
        return lowNode.val

    def pushAllNodes(self, root):
        while root is not None:
            self.stack.append(root)
            root = root.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
