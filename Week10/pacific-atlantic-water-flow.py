class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        pac, atl = set(), set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(i, j, prev, visited):
            if (i, j) in visited or i < 0 or i >= rows or j < 0 or j >= cols or heights[i][j] < prev:
                return
            visited.add((i, j))
            dfs(i + 1, j, heights[i][j], visited)
            dfs(i - 1, j, heights[i][j], visited)
            dfs(i, j + 1, heights[i][j], visited)
            dfs(i, j - 1, heights[i][j], visited)

        for i in range(rows):
            dfs(i, 0, 0, pac)
            dfs(i, cols - 1, 0, atl)
        for i in range(cols):
            dfs(0, i, 0, pac)
            dfs(rows - 1, i, 0, atl)
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res