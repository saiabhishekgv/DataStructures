"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        def preordertraversal(root, output=[]):
            if not root:
                return output

            if not root.children:
                output += [root.val]
                return output

            for i in root.children:
                output = preordertraversal(i, output)

            output += [root.val]
            return output

        return preordertraversal(root)