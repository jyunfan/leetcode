# Topics: Heap (Priority Queue)

import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        A = [(nums[i], i) for i in range(n)]
        heapq.heapify(A)

        score = 0
        while A:
            (k, idx) = heapq.heappop(A)
            print('get k', k, 'at', idx)
            if marked[idx]:
                continue
            marked[idx] = True
            if idx > 0:
                marked[idx-1] = True
            if idx < n - 1:
                marked[idx+1] = True
            score += k
            print('score', score)
        return score
