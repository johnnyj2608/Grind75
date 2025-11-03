class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complements:
                return [complements[complement], i]
            
            complements[nums[i]] = i