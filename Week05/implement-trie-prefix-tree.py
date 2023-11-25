class TreeNode():
    def __init__(self):
        self.children = {}
        self.end = False


class Trie(object):

    def __init__(self):
        self.node = TreeNode()

    def insert(self, word):
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

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ptr = self.node
        for i in word:
            if i not in ptr.children:
                return False
            ptr = ptr.children[i]
        return ptr.end == True

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        ptr = self.node
        for i in prefix:
            if i not in ptr.children:
                return False
            ptr = ptr.children[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)