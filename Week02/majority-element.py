class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        majority = 0

        for i in nums:
            if majority == 0:
                res = i

            if i == res:
                majority += 1
            else:
                majority -= 1
        return res
