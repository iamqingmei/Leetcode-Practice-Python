"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2): #72 ms
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        head = res
        while(l1 and l2): #l1 l2 both true
            if (l2.val < l1.val):
                res.next = l2
                l2=l2.next
            else:
                res.next = l1
                l1=l1.next
            res=res.next
        if (l2): #l1 not true, l2 true
            res.next=l2
        if (l1):
            res.next = l1
        return head.next

    def mergeTwoLists(self, l1, l2): #65 ms
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 is None):
            if (l2 is None): #both None
                return None
            return l2
        elif (l2 is None):
            return l1

        res = ListNode(-1)
        head = res
        while(l1 and l2): #l1 l2 both true
            if (l2.val < l1.val):
                res.next = l2
                l2=l2.next
            else:
                res.next = l1
                l1=l1.next
            res=res.next
        if (l2): #l1 not true, l2 true
            res.next=l2
        if (l1):
            res.next = l1
        return head.next

