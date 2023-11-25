class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        forw = [1]
        back = [1]
        res = [0] * len(nums)

        for i in range(len(nums) - 1):
            forw.append(forw[i] * nums[i])
        nums = nums[::-1]
        for i in range(len(nums) - 1):
            back.append(back[i] * nums[i])
        back = back[::-1]
        for i in range(len(res)):
            res[i] = forw[i] * back[i]
        return res