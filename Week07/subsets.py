class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, ind, path, res):
        res.append(list(path))
        for i in range(ind, len(nums)):
            if nums[i] not in path:
                self.dfs(nums, i, path + [nums[i]], res)
