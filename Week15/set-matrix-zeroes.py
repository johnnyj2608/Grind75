class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = 1

        # Marking which rows/cols need to be zeros
        for R in range(ROWS):
            for C in range(COLS):
                if matrix[R][C] == 0:
                    matrix[0][C] = 0  # Marks column to be 0
                    if R > 0:
                        matrix[R][0] = 0
                    else:
                        rowZero = 0

        # If row/col had a zero, make cell a zero
        for R in range(1, ROWS):
            for C in range(1, COLS):
                if matrix[0][C] == 0 or matrix[R][0] == 0:
                    matrix[R][C] = 0

        # Finally set each row/col to be zeros
        if matrix[0][0] == 0:
            for R in range(ROWS):
                matrix[R][0] = 0
        if rowZero == 0:
            for C in range(COLS):
                matrix[0][C] = 0