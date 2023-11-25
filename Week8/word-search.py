class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        charCount = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] not in charCount:
                    charCount[board[i][j]] = 0
                charCount[board[i][j]] += 1
        for i in word:
            if i in charCount and charCount[i] > 0:
                charCount[i] -= 1
            else:
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, 0, i, j):
                        return True
        return False

    def dfs(self, board, word, index, i, j):
        if len(word) == index:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False
        copy = board[i][j]
        board[i][j] = '#'
        if (self.dfs(board, word, index + 1, i + 1, j) or
                self.dfs(board, word, index + 1, i - 1, j) or
                self.dfs(board, word, index + 1, i, j + 1) or
                self.dfs(board, word, index + 1, i, j - 1)):
            return True
        board[i][j] = copy
