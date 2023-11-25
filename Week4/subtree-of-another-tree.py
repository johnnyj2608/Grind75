# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if subRoot == None:
            return True
        elif root == None:
            return False
        elif self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None or p.val != q.val:
            return False
        else:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)