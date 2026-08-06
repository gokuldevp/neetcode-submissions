class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_count = min([len(word) for word in strs])
        for i in range(smallest_count):
            ch = strs[0][i]
            for word in strs[1:]:
                if ch != word[i]:
                    return word[:i]
        return strs[0][:smallest_count]