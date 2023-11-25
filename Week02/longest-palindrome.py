class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = Counter(s)
        res = 0
        for i in s:
            res += s[i] / 2 * 2
            if res % 2 == 0 and s[i] % 2 == 1:
                res += 1
        return res

