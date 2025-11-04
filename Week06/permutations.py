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

        def dfs(path, visited):
            if len(nums) == len(path):
                res.append(list(path))
                return
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                path.append(nums[i])
                visited.add(nums[i])
                dfs(path, visited)
                path.pop()
                visited.remove(nums[i])

        dfs([], set())
        return res