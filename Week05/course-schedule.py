class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        cycle = set()
        visited = set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for i in adj[crs]:
                if dfs(i) == False:
                    return False
            visited.add(crs)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True

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
