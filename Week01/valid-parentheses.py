class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        para = {'}': '{', ')': '(', ']': '['}
        stack = []

        for i in s:
            if i in para and len(stack) > 0:
                if para[i] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0