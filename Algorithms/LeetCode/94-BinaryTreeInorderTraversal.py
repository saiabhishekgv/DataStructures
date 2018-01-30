'''

Question 94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''
'''
Resources : 
    1. https://leetcode.com/problems/binary-tree-inorder-traversal/solution/
    2. https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31231
'''

'''
Solution : 
    1. Recursive : 
        - Time Complexity : O(n)
        - Space Complexity : O(n) (Avg. case = O( log n))
    2. Iterative : 
        - Time COmplexity : O(n)
        - Space Complexity : O(n)
    3. Morris Traversal : 
        - Time Complexity : O(n)
        - Space Complexity : O(1)

'''

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        if root is None:
            return result
        stack.append(root.right)
        stack.append(root)
        stack.append(root.left)
        while len(stack) != 0:
            if stack.right is not None:
                stack.append(right)
            if stack.left is not None:
                stack.append(left)
