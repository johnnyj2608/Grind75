class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        
        for j in range(len(strs[0])):
            for i in range(len(strs)):
                if j == len(strs[i]) or strs[0][j] != strs[i][j]:
                    return res
            res += strs[0][j]
        
        return res
