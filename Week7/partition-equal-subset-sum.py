class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sums = sum(nums)
        if sums % 2 != 0:
            return False

        target = sums // 2
        dp = set([0])
        for n in nums:
            nextdp = set()
            for i in dp:
                nextdp.add(i + n)
                nextdp.add(i)
            if target in nextdp:
                return True
            dp = nextdp
        return False