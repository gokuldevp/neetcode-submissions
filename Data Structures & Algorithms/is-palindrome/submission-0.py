class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ch.lower() for ch in s if ch.isalnum()]
        print(s)
        length = len(s)
        for i in range(length//2):
            if s[i] != s[length-i-1]:
                return False
        return True