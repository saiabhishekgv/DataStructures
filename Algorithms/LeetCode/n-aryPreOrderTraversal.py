"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        def preordertraversal(root, output=[]):
            if not root:
                return output

            output += [root.val]

            if not root.children:
                return output

            for i in root.children:
                output = preordertraversal(i, output)

            return output

        return preordertraversal(root)