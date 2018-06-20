'''

Question 508. Most Frequent Subtree Sum

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

'''

'''
Resources : 
    1. https://leetcode.com/problems/most-frequent-subtree-sum/discuss/98749/Python-clean-solution-beats-97
    2. https://leetcode.com/problems/most-frequent-subtree-sum/discuss/98675/Python-easy-understand-solution
'''

'''
Solution : 
    1. Hashmap  + inorder : 
        - Time : O(n)
        - Space : O(n)
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        import collections
        if not root:
            return []

        c = collections.Counter()

        def inorder(root):
            if root is None:
                return 0
            s = root.val + inorder(root.left) + inorder(root.right)
            c[s] += 1
            return s

        inorder(root)
        frequent = max(c.values())
        return [s for s in c.keys() if c[s] == frequent]