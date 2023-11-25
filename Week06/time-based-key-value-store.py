class TimeMap(object):

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ""
        cur = self.store.get(key, [])

        left, right = 0, len(cur) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if cur[mid][1] == timestamp:
                return cur[mid][0]
            if cur[mid][1] < timestamp:
                res = cur[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)