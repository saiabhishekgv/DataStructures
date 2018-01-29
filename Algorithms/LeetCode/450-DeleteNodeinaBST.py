
'''
Question 450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
'''

'''
Resources : 
    1. https://leetcode.com/problems/delete-node-in-a-bst/discuss/93296
    2. https://leetcode.com/problems/delete-node-in-a-bst/discuss/93351
'''

'''
Solution : 
    1. Recursion :
        - Time Complexity : O(h) 
        - Runtime: 128 ms
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None :
            return None
        elif root.val < key :
            root.right =  self.deleteNode(root.right,key)
        elif root.val > key :
            root.left = self.deleteNode(root.left,key)
        else:
            if root.left is None:
                return root.right
            if root.right is None :
                return root.left
            else:
                temp = root.right
                predecessor = temp.val
                while temp.left:
                    temp = temp.left
                    predecessor  = temp.val
                root.val = predecessor
                root.right = self.deleteNode(root.right,root.val)
        return root