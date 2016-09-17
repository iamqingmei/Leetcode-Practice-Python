"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head): #45ms
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre,first= head,head
        if (head):
            head = head.next 
            
        while(head):
            if (head.val < pre.val): 
                #since it is a sorted array, next one smaller than previous one means looping
                break;
            if (pre.val == head.val):
                pre.next= head.next
            else:
                pre = head
            head = head.next
        return first