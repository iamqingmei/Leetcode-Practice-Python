"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes v and w as the lowest node in T 
that has both v and w as descendants (where we allow a node to be a descendant of itself).”
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. 
Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q): #172ms
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        plist=[]
        qlist=[]
        self.traverse(root,p,plist)
        self.traverse(root,q,qlist)
        for i in qlist:
            if i in plist:
                return i;
        return None;
        
    def traverse(self,root,node,nodelist):
        if (root is None):
            return False
        elif(root is node):
            #found
            nodelist.append(root)
            return True
        if (self.traverse(root.left,node,nodelist) or self.traverse(root.right,node,nodelist)):
            nodelist.append(root)
            return True
        else:
            return False


class Solution(object):
    def lowestCommonAncestor(self, root, p, q): #135ms
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root