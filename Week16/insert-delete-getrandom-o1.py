class RandomizedSet(object):

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.numMap:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.numMap:
            index = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[index] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = index
            self.numMap.pop(val)
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.numList)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()