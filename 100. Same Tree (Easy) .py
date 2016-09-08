"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q): #42ms
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p is None):
            if(q is None):
                return True 
            else:
                return False
        if (q is None): #p is not None
            return False
        #p q both not none
        if (p.val != q.val):
            return False
        return (self.isSameTree(p.left,q.left) & self.isSameTree(p.right,q.right))


    def isSameTree(self, p, q): #39ms
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if ((p is None) & (q is None)):
            return True
        if (q is None): #p is not None
            return False
        if (p is None): #q is not None
            return False
        #p q both not none
        if (p.val != q.val):
            return False
        return (self.isSameTree(p.left,q.left) & self.isSameTree(p.right,q.right))