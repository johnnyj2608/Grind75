class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        sign = 1
        s = s.strip()
        for i in range(len(s)):
            if i == 0 and s[i] == '-':
                sign *= -1
            elif i == 0 and s[i] == '+':
                continue
            elif s[i].isdigit():
                res = res*10 + int(s[i])
            else:
                break
        res *= sign
        if res < -2**31:
            return -2**31
        if res > 2**31 -1:
            return 2**31 -1
        return res