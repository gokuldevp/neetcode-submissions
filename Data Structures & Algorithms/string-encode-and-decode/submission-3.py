class Solution:

    def encode(self, strs: List[str]) -> str:
        if not list:
            return ""

        lengths = list()
        for s in strs:
            lengths.append(str(len(s)))
            lengths.append(",")
        lengths.append("#")

        lengths.extend(strs)

        return "".join(lengths)


        

    def decode(self, s: str) -> List[str]:
        if not s:
            return [""]

        lengths, strs = s.split("#",1)

        lengths = [int(l) for l in lengths.split(",")[:-1]]
   
        result = []
        
        length = len(strs)

        base = 0

        for l in lengths:
            result.append(strs[base:base+l])
            base += l

        return result




