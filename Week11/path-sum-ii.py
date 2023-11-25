# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, root, tar, path, res):
        if root == None:
            return
        if tar == root.val and root.left == None and root.right == None:
            res.append(path + [root.val])
            return
        self.dfs(root.left, tar - root.val, path + [root.val], res)
        self.dfs(root.right, tar - root.val, path + [root.val], res)