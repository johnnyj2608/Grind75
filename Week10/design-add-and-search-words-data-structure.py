class TreeNode():
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary(object):

    def __init__(self):
        self.node = TreeNode()
        self.max_length = 0

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        ptr = self.node
        for i in word:
            if i not in ptr.children:
                ptr.children[i] = TreeNode()
            ptr = ptr.children[i]
        ptr.end = True

        self.max_length = max(self.max_length, len(word))

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) > self.max_length:
            return False

        def dfs(index, ptr):
            for i in range(index, len(word)):
                if word[i] == '.':
                    for j in ptr.children.values():
                        if dfs(i + 1, j):
                            return True
                    return False
                else:
                    if word[i] not in ptr.children:
                        return False
                    ptr = ptr.children[word[i]]
            return ptr.end

        return dfs(0, self.node)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)