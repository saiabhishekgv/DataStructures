''''
Link : https://leetcode.com/problems/add-two-numbers/description/

Question 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Solution :

Brute Force :
    Time Complexity : O(m+n) m=length of list1, n=length of list2
    Runtime: 139 ms
'''

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(None)
        temp_result = result

        while (l1 and l2):
            current_val = l1.val + l2.val + carry
            carry = current_val / 10
            current_val %= 10
            current_Node = ListNode(current_val)
            temp_result.next = current_Node
            temp_result = temp_result.next
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            current_val = l1.val + carry
            carry = current_val / 10
            current_val %= 10
            current_Node = ListNode(current_val)
            temp_result.next = current_Node
            temp_result = temp_result.next
            l1 = l1.next

        while l2 != None:
            current_val = l2.val + carry
            carry = current_val / 10
            current_val %= 10
            current_Node = ListNode(current_val)
            temp_result.next = current_Node
            temp_result = temp_result.next
            l2 = l2.next

        if carry != 0:
            current_val = carry
            current_Node = ListNode(current_val)
            temp_result.next = current_Node
            temp_result = temp_result.next

        return result.next

