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

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)
