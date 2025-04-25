class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = Counter(s)
        res = 0

        for i in s:
            if s[i] % 2 == 1 and res % 2 == 1:
                res -= 1
            res += s[i]
        return res

