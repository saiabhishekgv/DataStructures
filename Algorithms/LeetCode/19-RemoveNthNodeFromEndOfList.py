'''
Question 19. Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

'''
Resources : 
    1. https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/
'''

'''
Solution : 
    1. Two pass : 
        - Time Complexity O(2*n)
    2. One pass :
        - Time Complexity O(n)
        - Run Time : 45ms

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head

        first_pointer = head
        second_pointer = None
        length = 0

        for i in xrange(n + 1):
            if first_pointer:
                length += 1
                first_pointer = first_pointer.next
                second_pointer = first_pointer
            elif length == n:
                return head.next
            else:
                return head

        second_pointer = head

        while first_pointer:
            length += 1
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        if second_pointer:
            second_pointer.next = second_pointer.next.next
        elif length == n:
            head = head.next
        return head