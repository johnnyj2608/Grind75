class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        resR, resL = 0, 0
        for i in range(len(s)):
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if resR - resL < R - L:
                    resR, resL = R, L
                L -= 1
                R += 1
            L, R = i, i+1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if resR - resL < R - L:
                    resR, resL = R, L
                L -= 1
                R += 1
        return s[resL:resR+1]

    class Solution(object):
        def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: str
            """
            res = ""
            for i in range(len(s)):
                l, r = i, i
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if len(res) < r - l + 1:
                        res = s[l:r + 1]
                    l -= 1
                    r += 1
                l, r = i, i + 1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if len(res) < r - l + 1:
                        res = s[l:r + 1]
                    l -= 1
                    r += 1

            return res