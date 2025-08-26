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

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        dp = [False] * (target+1)
        dp[0] = True

        for n in nums:
            for i in range(target, n-1, -1):
                if dp[i-n]:
                    dp[i] = True
                if dp[-1]:
                    return True
        return False
