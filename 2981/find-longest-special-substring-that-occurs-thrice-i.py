from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        m = defaultdict(int)
        count = 1
        m[(s[0],1)] += 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
                for j in range(1, count+1):
                    m[(s[i],j)] += 1
            else:
                count = 1
                m[(s[i],1)] += 1
        #print(m)
        maxlen = -1
        for (ch, length) in m:
            if m[(ch, length)] >= 3:
                maxlen = max(maxlen, length)

        return maxlen

