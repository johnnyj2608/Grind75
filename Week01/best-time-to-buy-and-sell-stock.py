class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        mins = float('inf')

        for i in prices:
            mins = min(mins, i)
            res = max(res, i - mins)
        return res