class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * len(s)
        dp.append(True)

        for i in range(len(s) - 1, -1, -1):
            for j in wordDict:
                if len(j) + i <= len(s) and j == s[i:i + len(j)] and dp[i + len(j)] == True:
                    dp[i] = True
                    break
        return dp[0]