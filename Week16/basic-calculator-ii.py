class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur, prev, res = 0, 0, 0
        op = '+'

        for i in s + "##":
            if i == ' ':
                continue
            elif i.isdigit():
                cur = cur * 10 + int(i)
            else:
                if op == '*':
                    prev *= cur
                elif op == '/':
                    prev = int(float(prev) / cur)
                else:
                    res += prev
                    prev = cur
                    if op == '-':
                        prev *= -1

                cur = 0
                op = i

        return res