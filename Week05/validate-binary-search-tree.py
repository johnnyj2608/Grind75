# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root, mins, maxs):
        if root == None:
            return True
        if root.val <= mins or root.val >= maxs:
            return False
        else:
            return self.dfs(root.left, mins, root.val) and self.dfs(root.right, root.val, maxs)