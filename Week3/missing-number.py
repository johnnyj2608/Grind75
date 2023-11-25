class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)+1):
            res = res ^ i
        for i in range(len(nums)):
            res = res ^ nums[i]
        return res

        # return sum(range(len(nums)+1)) - sum(nums)

        # nums = set(nums)
        # for i in range(len(nums)):
        #     if i not in nums:
        #         return i
        # return len(nums)