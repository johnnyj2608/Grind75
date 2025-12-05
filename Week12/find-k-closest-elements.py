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
    
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        l, r = 0, len(arr)-1
        while l < r:
            m = (r+l)//2
            if arr[m] < x:
                l = m + 1
            else:
                r = m

        l, r = l-1, l
        for _ in range(k):
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[l]-x) < abs(arr[r]-x) or (abs(arr[l]-x) == abs(arr[r]-x) and arr[l] < arr[r]):
                l -= 1
            else:
                r += 1

        return arr[l+1:r]