class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # only add open paranthesis if open < n
        # only add a clothing parenthesis if closed < open
        # valid IIF open == closed == n

        stack = []
        res = []

        def dfs(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                dfs(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                dfs(openN, closedN + 1)
                stack.pop()

        dfs(0, 0)
        return res