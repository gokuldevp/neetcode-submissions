class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}

        for num in nums:
            tracker[num] = tracker.get(num, 0) + 1

        if len(tracker.keys())<=k:
            return list(tracker.keys())

        tracker = dict(sorted(tracker.items(), key=lambda item: item[1]))

        return list(tracker.keys())[-k:]