# Topics: sliding window, hash table, two pointers

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = Counter(s1)
        k = len(s1)
        subs2count = Counter(s2[0:k])
        if subs2count == s1count:
            return True
        for i in range(1, len(s2)-k+1):
            subs2count[s2[i-1]] -= 1
            subs2count[s2[i+k-1]] += 1
            if subs2count == s1count:
                return True
        return False
