# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #base case
        #Algorithm - Breadth First Traversal
        
        if root is None:
            return []
        stack, res = [], []
        stack.append(root)
        res.append([root.val])
        even = 1
        while len(stack)>0:
            tempNode, temp = [], []
            for node in stack:
                if node.left:
                    tempNode.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    tempNode.append(node.right)
                    temp.append(node.right.val)
            stack = tempNode[::]
            if even and len(temp)>0:
                res.append(temp[::-1])
                even = 0
            elif len(temp)>0:
                res.append(temp)
                even = 1
        return res
        