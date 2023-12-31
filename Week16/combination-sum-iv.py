class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        DP = {0: 1}

        for total in range(1, target + 1):
            DP[total] = 0
            for n in nums:
                DP[total] += DP.get(total - n, 0)
        return DP[target]