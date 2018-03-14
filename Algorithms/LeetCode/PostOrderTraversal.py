# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #base case
        
        #algorithm
        #using two stacks
        #Root Right Left --> stack
        #reverse stack gives --> Root Left Right
        
        #step1:
        #go to the rightmost node until you reach a null, concurrently
        #add every node you traverse through, to the stack and append to result
        
        #step2:
        #when your current node is null and stack has elements in it
        #and assign current node as stack's top left
        #pop top of stack
        
        #step 3:
        #when stack and current node point to null, return result
        
        result, stack = [], []
        #implementation:
        if root is None:
            return result
        currentNode = root
        while True:
            if currentNode:
                stack.append(currentNode)
                result.append(currentNode.val)
                currentNode = currentNode.right
            if currentNode is None and stack:
                currentNode = stack[-1].left
                stack.pop(-1)
            if currentNode is None and len(stack)==0:
                return result[::-1]