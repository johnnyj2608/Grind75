class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        res = 0

        for i in nums:
            if (i - 1) not in numSet:
                cur = 0
                while (i + cur) in numSet:
                    cur += 1
                res = max(res, cur)
        return res