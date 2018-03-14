# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #base case
        #root is empty, then return an empty list
        
        #Root,Left,Right Traversal
        #Algorithm
        
        #step1:
        #go to each left of each node from root while adding it to result and pushing it to stack concurrently
        
        #step2:
        #when I hit a null, I'll set my current pointer to the top of stack's node's right node and
        #repeat step2
        
        #step3:
        #the loop stops once, my stack is empty and my current node is pointing to null.
        #this means by now, I have traversed all nodes in the tree.
        
        res, stack = [], []
        if root is None:
            return res
        currentNode = root
        while True:
            if currentNode:
                res.append(currentNode.val)
                stack.append(currentNode)
                currentNode = currentNode.left
            if currentNode is None and stack :
                currentNode = stack[-1].right
                stack.pop(-1)
            if currentNode is None and len(stack)==0:
                return res
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            