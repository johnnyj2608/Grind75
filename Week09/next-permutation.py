class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pivot = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i
                break
        if pivot == 0:
            nums.sort()
            return

        swap = len(nums) - 1
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1
        nums[swap], nums[pivot - 1] = nums[pivot - 1], nums[swap]
        nums[pivot:] = sorted(nums[pivot:])