# Easy
# Topics: heapq
# Notice that the smallest element is always the root.

import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        A = [-x for x in gifts]
        heapq.heapify(A)
        for i in range(k):
            v = -heapq.heappop(A)
            heapq.heappush(A, -math.floor(math.sqrt(v)))
        return -sum(A)
