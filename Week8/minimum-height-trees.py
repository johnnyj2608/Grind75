class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n < 2:
            return [0]

        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        leaves = []
        for i in adj:
            if len(adj[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            level = []
            for leaf in leaves:
                for neighbor in adj[leaf]:
                    adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    level.append(neighbor)
            leaves = level

        return leaves