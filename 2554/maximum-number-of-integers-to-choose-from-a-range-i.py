class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        c = 0
        s = 0
        bset = set(banned)
        for i in range(1, n+1):
            if i not in bset and s + i <= maxSum:
                s += i
                c += 1
                print(i, s)
        return c
