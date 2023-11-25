class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        res = 0
        cur = x
        while cur != 0:
            res = res * 10 + (cur % 10)
            cur = cur // 10
        return x == res