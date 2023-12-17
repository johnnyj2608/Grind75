class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0

        L = 0
        max_freq = 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            max_freq = max(max_freq, count[s[R]])
            while (R - L + 1) - max_freq > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
        return res