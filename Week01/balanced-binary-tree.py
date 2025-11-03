# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root):
            if root == None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1
            return max(l, r)+1

        res = dfs(root)
        if res == -1:
            return False
        return True