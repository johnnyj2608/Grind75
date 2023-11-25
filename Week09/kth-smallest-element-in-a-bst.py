# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None:
            return None
        res = []
        self.inorder(root, res)
        return res[k - 1]

    def inorder(self, root, res):
        if root == None:
            return
        left = self.inorder(root.left, res)
        res.append(root.val)
        right = self.inorder(root.right, res)