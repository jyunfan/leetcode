# Topics: priority queue

import heapq

def gain(p, t):
    return (p+1)/(t+1) - p/t

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        C = [(-gain(p,t), p, t) for (p, t) in classes]
        heapq.heapify(C)

        for i in range(extraStudents):
            (_, p, t) = heapq.heappop(C)
            heapq.heappush(C, (-gain(p+1, t+1), p+1, t+1))

        total_pass_ratio = 0
        for (_, p, q) in C:
            total_pass_ratio += p/q
        return total_pass_ratio / len(classes)
