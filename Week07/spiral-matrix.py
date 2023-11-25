class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        L, R = 0, len(matrix[0]) - 1
        T, B = 0, len(matrix) - 1

        res = []
        while L <= R and T <= B:
            for i in range(L, R + 1):
                res.append(matrix[T][i])
            T += 1
            for i in range(T, B + 1):
                res.append(matrix[i][R])
            R -= 1

            if not (L <= R and T <= B):
                return res

            for i in range(R, L - 1, -1):
                res.append(matrix[B][i])
            B -= 1
            for i in range(B, T - 1, -1):
                res.append(matrix[i][L])
            L += 1
        return res