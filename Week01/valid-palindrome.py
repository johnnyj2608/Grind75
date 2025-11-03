class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        s = s.lower()
        while l<r:
            if s[l] in string.punctuation or s[l] == ' ':
                l += 1
            elif s[r] in string.punctuation or s[r] == ' ':
                r -= 1
            elif s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace(' ', '').lower()
        for i in string.punctuation:
            s = s.replace(i, '')
        
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True