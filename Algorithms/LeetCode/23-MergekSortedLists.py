'''
Link : https://leetcode.com/problems/merge-k-sorted-lists/description/

Question 23. Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

'''
Resources : 
    1. https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511
    2. https://leetcode.com/problems/merge-k-sorted-lists/discuss/10527
'''
'''
Solution : 
    1. Priority Queue : 
        - Time Complexity : O(n)
        - Space Complexity : O(K)
        - Runtime: 378 ms 
'''

from Queue import PriorityQueue

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = PriorityQueue()
        for l in lists:
            if l:
                pq.put((l.val, l))

        res = []

        while not pq.empty():
            val, node = pq.get()
            res.append(val)
            node = node.next
            if node:
                pq.put((node.val, node))

        return res