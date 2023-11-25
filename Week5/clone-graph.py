"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None
        oldNew = {}
        return self.dfs(node, oldNew)

    def dfs(self, node, oldNew):
        if node in oldNew:
            return oldNew[node]
        copy = Node(node.val)
        oldNew[node] = copy
        for i in node.neighbors:
            copy.neighbors.append(self.dfs(i, oldNew))
        return copy