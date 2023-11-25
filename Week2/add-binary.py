class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        c = 0
        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            cur = c
            if i < len(a):
                cur += int(a[i])
            if i < len(b):
                cur += int(b[i])
            c = cur // 2
            res += str(cur % 2)
        if c > 0:
            res += str(c)
        return res[::-1]
