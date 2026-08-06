class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        tracker = {}

        for num in nums:
            tracker[num] = tracker.get(num, 0) + 1

        n_3 = len(nums)//3
        
        return [k for k,v in tracker.items() if v>n_3]

