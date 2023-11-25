class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks = Counter(tasks)
        heap = []
        for i in tasks:
            heapq.heappush(heap, tasks[i]*-1)
        queue = deque()
        time = 0
        while heap or queue:
            time += 1
            if heap:
                cur = heapq.heappop(heap)+1
                if cur:
                    queue.append([cur, time+n])
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time