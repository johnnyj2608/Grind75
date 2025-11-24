class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []

        def binarySearch(l, r, tar):
            while l < r:

                m = (r+l)//2
                if res[m] == tar:
                    return m
                if tar < res[m]:
                    r = m
                else:
                    l = m + 1
            return l

        for i in nums:
            if len(res) == 0 or res[-1] < i:
                res.append(i)
            else:
                index = binarySearch(0, len(res)-1, i)
                res[index] = i
        return len(res)

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
