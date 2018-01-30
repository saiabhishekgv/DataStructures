'''
Question 101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''
'''
Resources : 
    1. https://leetcode.com/problems/symmetric-tree/solution/
    2. https://leetcode.com/problems/symmetric-tree/discuss/33054
'''
'''
Solution : 
    1. Using two queues :
        - Time Complexity : O(n)
        - Run time : 45 ms    
    2.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        leftElements = [root.left]
        rightElements = [root.right]

        while len(leftElements) != 0 and len(rightElements) != 0:
            leftElement = leftElements[0]
            del leftElements[0]
            rightElement = rightElements[0]
            del rightElements[0]
            check = [i is None for i in [leftElement, rightElement]]
            if all(check):
                continue
            elif any(check):
                return False
            elif leftElement.val != rightElement.val:
                return False
            else:
                leftElements.append(leftElement.left)
                leftElements.append(leftElement.right)
                rightElements.append(rightElement.right)
                rightElements.append(rightElement.left)

        return len(leftElements) == len(rightElements) and len(leftElements) == 0
