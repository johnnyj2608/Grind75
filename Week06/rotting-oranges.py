class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        fresh = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while q and fresh:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                    dx += x
                    dy += y
                    if dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0]) or grid[dx][dy] != 1:
                        continue
                    grid[dx][dy] = 2
                    q.append((dx, dy))
                    fresh -= 1
            res += 1
        if fresh:
            return -1
        return res
