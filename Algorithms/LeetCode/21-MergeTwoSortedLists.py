'''
Link : https://leetcode.com/problems/merge-two-sorted-lists/description/

Question 21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

''' 
Resources : 
    1. https://leetcode.com/problems/merge-two-sorted-lists/solution/ 
    2. 
'''
'''
Solution : 
    1. Linear Merge : 
        - Time Complexity : O(m+n)
        - Space Complexity : O(1)
        - Run time : 56 ms
'''


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return head.next