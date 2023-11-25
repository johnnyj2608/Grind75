class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = Counter(magazine)

        for i in ransomNote:
            if i in magazine and magazine[i] > 0:
                magazine[i] -= 1
            else:
                return False
        return True