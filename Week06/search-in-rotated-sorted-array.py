class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L, R = 0, len(nums) - 1
        while L <= R:
            M = L + (R - L) // 2
            if target == nums[M]:
                return M
            if nums[M] > nums[L]:  # L sorted
                if target < nums[L] or target > nums[M]:
                    L = M + 1
                else:
                    R = M - 1
            else:
                if target < nums[M] or target > nums[R]:
                    R = M - 1
                else:
                    L = M + 1

        return -1