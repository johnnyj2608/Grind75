class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""    # res = []
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
            res += str(cur % 2)     # n^2, copying string
        if c > 0:
            res += str(c)
        return res[::-1]

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        c = 0

        indexA, indexB = len(a)-1, len(b)-1

        while indexA >= 0 or indexB >= 0 or c == 1:
            if indexA >= 0:
                c += int(a[indexA])
                indexA -= 1
            if indexB >= 0:
                c += int(b[indexB])
                indexB -= 1
            
            res += str(c % 2)
            c = c // 2

        return res[::-1]