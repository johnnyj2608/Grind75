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

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        duplicates = set()
        res = 0

        for i in s:
            if i in duplicates:
                duplicates.remove(i)
                res += 2
            else:
                duplicates.add(i)
        
        if duplicates:
            res += 1
        return res
