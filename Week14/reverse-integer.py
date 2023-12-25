class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31
        sign = 1
        res = 0

        if x < 0:
            sign = -1
            x *= -1

        while x:
            digit = x % 10
            x = x // 10
            res = res * 10 + digit
        res *= sign

        if res > max_int or res < min_int:
            return 0
        return res