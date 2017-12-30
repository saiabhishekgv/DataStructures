'''

Link : https://leetcode.com/problems/swap-nodes-in-pairs/description/

Question 24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

'''
Resources :
    1. https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11019
    2. 
'''

'''
Solution : 
    1. Single pass and swap: 
        - Time Complexity : O(n)
        - Space Complexity : O(1)
        - Run Time : 36 ms
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return head

        currentnode = head
        while currentnode and currentnode.next:
            nextnode = currentnode.next
            currentnode.val, nextnode.val = nextnode.val, currentnode.val
            # for links
            # prevnode.next, nextnode.next, currentnode.next = nextnode, currentnode, nextnode.next

            currentnode = nextnode.next

        return head

