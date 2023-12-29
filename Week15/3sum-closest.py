class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = float('inf')
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                three = nums[i] + nums[left] + nums[right]
                if three == target:
                    return target
                if three < target:
                    left += 1
                else:
                    right -= 1
                if abs(three-target) < abs(res-target):
                    res = three
        return res