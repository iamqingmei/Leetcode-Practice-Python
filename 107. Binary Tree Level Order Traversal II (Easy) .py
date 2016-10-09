"""
Given a binary tree, 
return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root): #75 ms 24%
        if not root:
            return []

        level_dict = {}

        def reverse_tree(r, level):
            if not r:
                return

            if level in level_dict:
                level_dict[level].append(r.val)
            else:
                level_dict[level] = [r.val]
        # print(level_dict)

            if r.left:
                reverse_tree(r.left, level+1)

            if r.right:
                reverse_tree(r.right, level+1)

        reverse_tree(root, 0)

        bottom_up_lst = [level_dict[l] for l in sorted(level_dict, reverse=True)]

        return bottom_up_lst
