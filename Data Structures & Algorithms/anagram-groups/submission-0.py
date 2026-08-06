class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if tracker.get(sorted_word):
                tracker[sorted_word].append(word)
            else:
                tracker[sorted_word] = [word]

        return list(tracker.values())