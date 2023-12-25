class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        while top <= bot:
            row = top + (bot - top) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        l, r = 0, cols - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target > matrix[row][mid]:
                l += 1
            elif target < matrix[row][mid]:
                r -= 1
            else:
                return True
        return False