'''
Question 144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
'''
'''
Resources : 
    1.
    2.
'''
'''
Solution :
    1. Recursive : 
        - Time complexity : O(n)
        - Run time :37ms
    2. Iterative : 
        - Time Complexity : O(n)
        -Space Complexity : O(n)
'''


class Solution(object):
    def preorderTraversal_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.preOrderRecur(root, [])

    def preOrderRecur(self, root, result):
        if root is None:
            return result
        result.append(root.val)
        if root.left is not None:
            self.preOrderRecur(root.left, result)
        if root.right is not None:
            self.preOrderRecur(root.right, result)
        return result