class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, cand, tar, ind, path, res):
        if tar == 0:
            res.append(list(path))
            return
        elif tar < 0:
            return
        for i in range(ind, len(cand)):
            self.dfs(cand, tar - cand[i], i, path + [cand[i]], res)

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(candidates, target, 0, res, [])
        return res

    def dfs(self, cand, tar, ind, res, path):
        if tar == 0:
            res.append(path)
            return
        if tar < 0:
            return
        for i in range(ind, len(cand)):
            path.append(cand[i])
            self.dfs(cand, tar - cand[i], i, res, list(path))
            path.pop()