class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[pre].append(crs)
        visited = set()
        for i in range(numCourses):
            if self.dfs(i, visited, adj) == False:
                return False
        return True

    def dfs(self, crs, visited, adj):
        if adj[crs] == []:
            return True
        if crs in visited:
            return False
        visited.add(crs)
        for i in adj[crs]:
            if self.dfs(i, visited, adj) == False:
                return False
        adj[crs] = []
