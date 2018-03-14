# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack, res = [], []
        if root is None:
            return res
        currentNode = root
        stack.append(currentNode)
        res.append([currentNode.val])
        while len(stack)>0:
            tempstack, temp = [], []
            for node in stack:
                if node.left:
                    tempstack.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    tempstack.append(node.right)
                    temp.append(node.right.val)
            stack = tempstack[::]
            if len(temp)!=0:
                res.append(temp)
        return res
                