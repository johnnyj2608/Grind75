class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for i in points:
            x, y = i[0], i[1]
            dist = ((x - 0) ** 2 + (y - 0) ** 2) ** 0.5
            if len(heap) < k:
                heapq.heappush(heap, [dist * -1, i])
            else:
                heapq.heappushpop(heap, [dist * -1, i])
        return [x[1] for x in heap]
