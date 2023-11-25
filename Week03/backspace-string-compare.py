class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.build(s) == self.build(t)
    def build(self, word):
        stack = []
        for i in word:
            if i != '#':
                stack.append(i)
            elif stack:
                stack.pop()
        return stack