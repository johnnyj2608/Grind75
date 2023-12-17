# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        q = deque()  # [node, num, level]
        prevLevel, firstNum = 0, 1

        if root == None:
            return res

        q.append([root, 1, 0])

        while q:
            node, num, level = q.popleft()

            if level > prevLevel:
                prevLevel = level
                firstNum = num
            res = max(res, num - firstNum + 1)

            if node.left:
                q.append([node.left, 2 * num, level + 1])
            if node.right:
                q.append([node.right, 2 * num + 1, level + 1])
        return res