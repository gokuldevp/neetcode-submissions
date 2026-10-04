class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        tracker = {}

        for l in s:
            tracker[l] = tracker.get(l,0) + 1

        for l in t:
            if l not in tracker:
                return False
            tracker[l] = tracker.get(l) - 1
            if tracker[l] == 0:
                del tracker[l]

        if tracker:
            return False

        return True
