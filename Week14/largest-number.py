class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        def compare(num1, num2):
            if num1 + num2 > num2 + num1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int(''.join(nums)))  # Makes [0, 0, 0] = "0"