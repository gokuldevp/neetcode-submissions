class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for k,v in enumerate(nums):
            v2 = target - v
            if v2 in tracker:
                return [tracker[v2], k]
            tracker[v] = k