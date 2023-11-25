class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        sCount, pCount = {}, {}
        res = []
        for i in range(len(p)):
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            pCount[p[i]] = pCount.get(p[i], 0) + 1
        if pCount == sCount:
            res.append(0)
        L = 0
        for R in range(len(p), len(s)):
            sCount[s[R]] = sCount.get(s[R], 0) + 1
            sCount[s[L]] -= 1
            if sCount[s[L]] == 0:
                sCount.pop(s[L])
            L += 1

            if pCount == sCount:
                res.append(L)
        return res