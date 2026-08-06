class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        length = len(arr)

        for i in range(length-1, -1, -1):
            temp =  arr[i]
            arr[i] = greatest
            if temp > greatest:
                greatest = temp

            
        return arr
