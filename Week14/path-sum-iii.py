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
        :rtype: int
        """
        self.res = 0
        self.cache = defaultdict(int)
        self.cache[targetSum] = 1

        def dfs(root, cur):
            if root == None:
                return
            cur += root.val
            self.res += self.cache.get(cur, 0)
            self.cache[cur + targetSum] += 1
            dfs(root.left, cur)
            dfs(root.right, cur)
            self.cache[cur + targetSum] -= 1

        dfs(root, 0)
        return self.res