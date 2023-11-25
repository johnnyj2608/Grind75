# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if root == None:
            return self.res

        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root == None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res = max(self.res, left + right)
        return max(left, right) + 1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        res = [0]
        self.dfs(root, res)
        return res[0]

    def dfs(self, root, res):
        if root == None:
            return 0
        left = self.dfs(root.left, res)
        right = self.dfs(root.right, res)
        res[0] = max(res[0], (left + right))
        return max(left, right) + 1