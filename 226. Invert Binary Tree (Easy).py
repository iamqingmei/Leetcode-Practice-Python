"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (root): 
            inverting(root)
        return root

def inverting(root):
    if root.left==None and root.right == None: 
        return
    if (root.left):
        inverting (root.left)
    if (root.right):
        inverting (root.right)
    temp = root.left
    root.left = root.right
    root.right = temp