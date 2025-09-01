class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                substr = ""
                while stack[-1] != '[':
                    substr=stack.pop()+substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop()+k
                stack.append(int(k)*substr)
        return "".join(stack)
    
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        cur = ""
        count = 0

        for i in s:
            if i == '[':
                stack.append(cur)
                stack.append(count)
                cur = ""
                count = 0
            elif i == ']':
                mult = stack.pop()
                prev = stack.pop()
                cur = prev + mult * cur
            elif i.isdigit():
                count = count * 10 + int(i)
            else:
                cur += i
        return cur