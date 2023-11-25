class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in rows[i] or
                        board[i][j] in cols[j] or
                        board[i][j] in sqrs[(i // 3, j // 3)]):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                sqrs[(i // 3, j // 3)].add(board[i][j])
        return True