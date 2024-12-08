# find x in A. If x not in A, find minimum v > x
# Becare of duplicate numbers in A
def search(x, A):
    left = 0
    right = len(A)-1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] < x:
            left = mid + 1
        else:
            # If A[mid]==x, we still try to find smallest y that A[y]==x
            right = mid - 1
            ans = mid
    return ans

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # sort events by start time in ascending order
        events.sort(key=lambda x: x[0])
        n = len(events)
        print(events)

        # all event start in orders
        starts = sorted([x[0] for x in events])

        # first phase: find maximum of one event >= index i
        first_max = [0] * len(events)
        first_max[-1] = events[-1][2]
        for i in range(n-2, -1, -1):
            s, e, v = events[i]
            first_max[i] = max(v, first_max[i+1])
        
        # second phase: find maximum of at most 2 events
        max_sum = [0] * len(events)
        # set max_sum for the last event
        max_sum[-1] = events[-1][2]

        # check every event backward
        n = len(events)
        for i in range(n-2, -1, -1):
            s, e, v = events[i]

            # case: not take the event i
            max_sum[i] = max_sum[i+1]

            # case: take the event i
            # find first position after end of event i
            pos = search(e+1, starts)
            if pos == -1:
                max_sum[i] = max(v, max_sum[i+1])
            else:
                max_sum[i] = max(v+first_max[pos], max_sum[i+1])

        return max_sum[0]
