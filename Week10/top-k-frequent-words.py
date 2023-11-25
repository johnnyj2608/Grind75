class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words = Counter(words)
        heap = []
        for i in words:
            heapq.heappush(heap, [words[i] * -1, i])

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res