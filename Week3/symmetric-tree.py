# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None or left.val != right.val:
            return False
        else:
            return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)