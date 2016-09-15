"""
Reverse a singly linked list.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head): #72ms
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while(head):
            head.next,pre,head = pre,head,head.next
        return pre
        