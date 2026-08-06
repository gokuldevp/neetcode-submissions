class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s1_l = len(haystack)
        s2_l = len(needle)

        for i in range(0, s1_l-s2_l+1):
            if haystack[i:i+s2_l] == needle:
                return i
        return -1