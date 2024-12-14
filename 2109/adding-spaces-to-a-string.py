class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        n = len(spaces)
        i = len(s) - 1
        for pos in spaces[::-1]:
            res.extend(s[pos:i+1][::-1])
            res.extend([' '])
            i = pos - 1
        res.extend(s[0:i+1][::-1])
        res = ''.join(res[::-1])
        return res
