class Solution:
    def isValid(self, s: str) -> bool:
        tracker = []

        static = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        for symbol in s:
            if symbol not in static:
                tracker.append(symbol)
            else:
                if not tracker:
                    return False
                if tracker[-1] != static[symbol]:
                    return False
                tracker.pop()

        return not tracker