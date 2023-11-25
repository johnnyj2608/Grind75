class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L, R = 0, len(height) - 1
        res = 0
        while L < R:
            area = R - L
            if height[L] < height[R]:
                area *= height[L]
                L += 1
            else:
                area *= height[R]
                R -= 1
            res = max(res, area)

        return res