class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length = len(s)
        longest = 0
        for i in range(length):
            current = 1
            seen = {s[i]}
            for j in range(i+1, length):
                if s[j] in seen:
                    break
                current += 1
                seen.add(s[j])
            if current > longest:
                longest = current
        return longest

