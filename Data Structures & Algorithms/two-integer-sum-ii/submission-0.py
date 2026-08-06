class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        track = {}

        for k,v in enumerate(numbers):
            dif = target - v
            if dif in track:
                return [track[dif]+1, k+1]
            track[v] = k