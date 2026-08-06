class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        maxi = max(num_set)
        mini = min(num_set)
        longest = 1
        length = 0
        for i in range(mini, maxi+1):
            if i in num_set:
                length += 1
                longest = max(longest,length)
            else:
                length = 0

        return longest

        
