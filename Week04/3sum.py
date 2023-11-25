class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L, R = i+1, len(nums)-1
            while L < R:
                Z = nums[i]+nums[L]+nums[R]
                if Z < 0:
                    L += 1
                elif Z > 0:
                    R -= 1
                else:
                    res.append([nums[i],nums[L],nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
        return res