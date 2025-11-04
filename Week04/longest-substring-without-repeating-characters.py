class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in s[l:r]:   # O(n^2)
                l += 1
            res = max(res, r - l + 1)
        return res

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, l = 0, 0
        visited = set()
        for r in range(len(s)):
            while s[r] in visited:  # O(n)
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            res = max(res, r - l + 1)

        return res