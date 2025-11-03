class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        def dfs(i, j, old):
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[i]) or image[i][j] != old or image[i][j] == color:
                return
            image[i][j] = color
            dfs(i+1, j, old)
            dfs(i-1, j, old)
            dfs(i, j+1, old)
            dfs(i, j-1, old)
        
        dfs(sr, sc, image[sr][sc])
        return image