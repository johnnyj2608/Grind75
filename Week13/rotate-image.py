class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        L, R = 0, len(matrix) - 1

        while L < R:
            for i in range(R - L):
                T, B = L, R

                # save the top left
                topL = matrix[T][L + i]

                # move bottom left into top left
                matrix[T][L + i] = matrix[B - i][L]

                # move bottom right into bottom left
                matrix[B - i][L] = matrix[B][R - i]

                # move top right into bottom right
                matrix[B][R - i] = matrix[T + i][R]

                # move top left into top right
                matrix[T + i][R] = topL
            L += 1
            R -= 1


