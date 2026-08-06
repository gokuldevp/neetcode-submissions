class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0,0,0]

        for num in nums:
            counter[num] += 1

        c = 0
        for k,v in enumerate(counter):
            while v:
                nums[c] = k
                c += 1
                v -= 1
        return nums