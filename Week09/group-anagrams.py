class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for i in range(len(strs)):
            anagram = ''.join(sorted(strs[i]))
            anagrams[anagram].append(strs[i])
        return anagrams.values()