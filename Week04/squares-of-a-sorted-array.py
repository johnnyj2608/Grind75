class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        L, R = 0, len(nums)-1
        while L <= R:
            if nums[L]**2>nums[R]**2:
                res.append(nums[L]**2)
                L += 1
            else:
                res.append(nums[R]**2)
                R -= 1
        return res[::-1]