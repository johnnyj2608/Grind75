# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.bst(nums, 0, len(nums) - 1)

    def bst(self, nums, left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        cur = TreeNode(nums[mid])
        cur.left = self.bst(nums, left, mid - 1)
        cur.right = self.bst(nums, mid + 1, right)
        return cur
