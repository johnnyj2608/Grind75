class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)

        cycle = set()
        visited = set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in adj[crs]:
                if dfs(pre) == False:
                    return []
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return res

