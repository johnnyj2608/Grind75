class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        para = {'}':'{', ']':'[', ')':'('}
        stack = []
        for i in s:
            if i in para:
                if stack and stack[-1] == para[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0