"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        output = []
        queue = []
        queue.append(root)
        while len(queue) != 0 :
            output.append([i.val for i in queue if i])
            l = len(queue)
            for i in range(l) :
                head = queue[0]
                del queue[0]
                if head :
                    queue = queue +  head.children
        return output