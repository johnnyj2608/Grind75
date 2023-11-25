class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mins = float('inf')
        res = 0

        for i in range(len(prices)):
            if i == 0:
                mins = prices[i]
            else:
                mins = min(mins, prices[i])
                res = max(res, prices[i] - mins)

        return res