class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        chunk = set()
        loc = set()
        counter = 0
        for i in range(n-1, -1, -1):
            chunk.add(arr[i])
            loc.add(i)
            if chunk == loc:
                counter += 1
                chunk.clear()
                loc.clear()
        return counter
