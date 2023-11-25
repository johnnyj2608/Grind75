# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        mapping = {}
        for i in range(len(inorder)):
            mapping[inorder[i]] = i
        preorder = deque(preorder)

        def build(L, R):
            if L > R:
                return
            root = TreeNode(preorder.popleft())
            mid = mapping[root.val]
            root.left = build(L, mid - 1)
            root.right = build(mid + 1, R)
            return root

        return build(0, len(preorder) - 1)