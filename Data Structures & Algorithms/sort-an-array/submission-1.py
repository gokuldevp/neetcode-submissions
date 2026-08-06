class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        mini = float("inf")
        maxi = float("-inf")

        for num in nums:
            if num > maxi:
                maxi = num
            if num < mini:
                mini = num

        dif = maxi-mini
        result = [0] * (dif+1)

        for num in nums:
            result[num-mini] += 1

        res = []
        for k,v in enumerate(result):
            if v:
                res.extend([k+mini]*v)

        return res


