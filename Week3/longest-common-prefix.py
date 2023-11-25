class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for i in range(len(min(strs))):
            letter = strs[0][i]
            for j in range(1, len(strs)):
                if letter != strs[j][i]:
                    return res
            res += letter
        return res