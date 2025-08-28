class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord('a')] +=1
            anagrams[tuple(count)].append(i)

        res = []
        for i in anagrams:
            res.append(anagrams[i])
        return res