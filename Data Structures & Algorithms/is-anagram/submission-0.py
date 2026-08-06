class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = {}

        for ele in s:
            tracker[ele] = tracker.get(ele, 0) + 1

        for ele in t:
            if not tracker.get(ele):
                return False
            tracker[ele] -= 1

        return max(tracker.values()) == 0