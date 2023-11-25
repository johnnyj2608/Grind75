class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if digits == None or len(digits) == 0:
            return res
        phone = {'2': "abc",
                 '3': "def",
                 '4': "ghi",
                 '5': "jkl",
                 '6': "mno",
                 '7': "pqrs",
                 '8': "tuv",
                 '9': "wxyz"}
        self.dfs(digits, phone, 0, "", res)
        return res

    def dfs(self, digits, phone, ind, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        letters = phone[digits[ind]]
        for i in range(len(letters)):
            self.dfs(digits, phone, ind + 1, path + letters[i], res)
