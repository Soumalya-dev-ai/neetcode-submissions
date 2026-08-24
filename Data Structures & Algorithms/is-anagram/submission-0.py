class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s and not t or s and not s or len(s)!=len(t):
            return False
        elif not s and not t:
            return True
        return sorted(s) == sorted(t)
        