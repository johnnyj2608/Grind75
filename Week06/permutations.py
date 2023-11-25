class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if len(path) == len(nums):
            res.append(list(path))
            return
        for i in range(len(nums)):
            if nums[i] not in path:
                self.dfs(nums, path + [nums[i]], res)

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, res, [])
        return res

    def dfs(self, nums, res, path):
        if len(nums) == len(path):
            res.append(path)
            return
        for i in range(len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                self.dfs(nums, res, list(path))
                path.pop()