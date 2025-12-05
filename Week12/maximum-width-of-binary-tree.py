# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        queue = deque()
        queue.append((root, 0))

        while queue:
            _, first_index = queue[0]
            
            for i in range(len(queue)):
                cur, index = queue.popleft()
                if cur.left:
                    queue.append((cur.left, index*2))
                if cur.right:
                    queue.append((cur.right, index*2+1))
            res = max(res, index - first_index + 1)
        return res