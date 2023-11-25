class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for i in range(len(nums)):
            if nums[i] in complements:
                return complements[nums[i]], i
            complements[target-nums[i]] = i
        return -1