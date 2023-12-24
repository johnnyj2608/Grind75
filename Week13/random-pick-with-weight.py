class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = []
        total = 0
        for weight in w:
            total += weight
            self.w.append(total)
        self.total = total

    def pickIndex(self):
        """
        :rtype: int
        """
        rand = random.randint(1, self.total)
        L, R = 0, len(self.w)
        while L <= R:
            M = L + (R - L) // 2
            if self.w[M] == rand:
                return M
            elif self.w[M] < rand:
                L = M + 1
            else:
                R = M - 1
        return L


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()