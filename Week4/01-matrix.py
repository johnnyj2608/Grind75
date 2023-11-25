class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = '#'

        while q:
            x, y = q.popleft()
            for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                dx += x
                dy += y
                if dx < 0 or dx >= len(mat) or dy < 0 or dy >= len(mat[0]) or mat[dx][dy] != '#':
                    continue
                mat[dx][dy] = mat[x][y] + 1
                q.append((dx, dy))
        return mat