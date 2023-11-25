class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        self.dfs(image, sr, sc, color, image[sr][sc])
        return image

    def dfs(self, grid, i, j, new, old):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == new or grid[i][j] != old:
            return
        grid[i][j] = new
        self.dfs(grid, i - 1, j, new, old)
        self.dfs(grid, i + 1, j, new, old)
        self.dfs(grid, i, j - 1, new, old)
        self.dfs(grid, i, j + 1, new, old)