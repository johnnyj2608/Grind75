class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] < intervals[i+1][0]:
                i += 1
            else:
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i)
        return intervals

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        merged = []
        for interval in intervals:
            if len(merged)==0 or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
    
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()

        res = []
        cur = None
        for start, end in intervals:
            if cur == None:
                cur = [start, end]
            elif cur[1] < start:
                res.append(cur)
                cur = [start, end]
            else:
                cur[0] = min(cur[0], start)
                cur[1] = max(cur[1], end)
        if cur:
            res.append(cur)
            
        return res