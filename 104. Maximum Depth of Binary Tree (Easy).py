"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return traverse(root)
        return 0
        
        
def traverse(root):
    leftCount = 0
    rightCount = 0
    if root.left == None and root.right == None: #leaf node
        return 1 #it self
    if (root.left):
        leftCount = traverse(root.left)
    if (root.right):
        rightCount = traverse(root.right)
    return max(leftCount, rightCount) + 1