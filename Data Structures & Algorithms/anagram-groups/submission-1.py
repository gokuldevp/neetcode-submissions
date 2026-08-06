class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in tracker:
                tracker[sorted_s] = []
            tracker[sorted_s].append(s)
            
        return list(tracker.values())