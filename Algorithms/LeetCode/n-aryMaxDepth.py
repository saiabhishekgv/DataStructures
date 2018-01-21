class Solution(object):
    def maxDepth(self, root, maxi=0):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1

        for i in root.children:
            getDepth = self.maxDepth(i)
            maxi = max(maxi, getDepth + 1)

        return maxi
