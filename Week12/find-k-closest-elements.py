class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        L, R = 0, len(arr) - k

        while L < R:
            M = L + (R - L) // 2

            if x - arr[M] > arr[M + k] - x:
                L = M + 1
            else:
                R = M
        return arr[L:L + k]