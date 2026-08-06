class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        for l in s:
            seen[l] = seen.get(l,0) + 1

        for l in t:
            if not seen.get(l):
                return False

            seen[l] = seen.get(l,0) - 1

        return True