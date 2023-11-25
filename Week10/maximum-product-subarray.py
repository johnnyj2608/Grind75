class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mins, maxs = 1, 1
        res = float('-inf')

        for i in nums:
            mins, maxs = min(i * mins, i * maxs, i), max(i * mins, i * maxs, i)
            res = max(res, mins, maxs)
        return res