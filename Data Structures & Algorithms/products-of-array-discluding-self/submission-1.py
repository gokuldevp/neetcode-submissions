class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        result = [1] * length

        for i in range(length):
            result[i] = mul(nums[:i]) * mul(nums[i+1:])

        return result
        
def mul(*args):
    result = 1
    for element in args[0]:
        result *= element

    return result

