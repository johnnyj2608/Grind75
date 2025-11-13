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

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mins, maxs = nums[0], nums[0]
        res = nums[0]

        for i in nums[1:]:
            if i < 0:
                mins, maxs = maxs, mins
            mins = min(mins*i, i)
            maxs = max(maxs*i, i)
            res = max(res, maxs)
        return res