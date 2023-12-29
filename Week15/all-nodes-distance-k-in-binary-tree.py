# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        adj = defaultdict(list)
        self.buildGraph(root, None, adj)

        q = deque()
        q.append(target)
        visited = set([target])

        while q and k:
            for i in range(len(q)):
                cur = q.popleft()

                for neighbor in adj[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            k -= 1

        res = []
        for i in q:
            res.append(i.val)
        return res

    def buildGraph(self, root, parent, adj):
        if root == None:
            return root

        if parent:
            adj[root].append(parent)
        if root.left:
            adj[root].append(root.left)
            self.buildGraph(root.left, root, adj)
        if root.right:
            adj[root].append(root.right)
            self.buildGraph(root.right, root, adj)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        adj = defaultdict(list)
        self.buildGraph(root, None, adj)

        q = deque()
        q.append((target, 0))
        visited = set([target])
        res = []

        while q:
            cur, dist = q.popleft()

            if dist == k:
                res.append(cur.val)
            if dist > k:
                break
            for neighbor in adj[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, dist + 1))
        return res

    def buildGraph(self, root, parent, adj):
        if root == None:
            return root

        if parent:
            adj[root].append(parent)
        if root.left:
            adj[root].append(root.left)
            self.buildGraph(root.left, root, adj)
        if root.right:
            adj[root].append(root.right)
            self.buildGraph(root.right, root, adj)