class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        L, R = 0, len(nums) - 1
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1

        L, R = 0, k - 1
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1

        L, R = k, len(nums) - 1
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1