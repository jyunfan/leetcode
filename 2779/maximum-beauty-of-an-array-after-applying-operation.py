# Topic: Line sweep

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # reduce the problem to the interval problem
        # a element i and become (i-k, i+k)

        # when enter an interval, increase the count by 1
        # when leave an interval, decrease the count by 1
        # a trick: I add a small number 0.1 to interval end to ensure interval_begin appears before interval_end
        points = [[i-k, 1] for i in nums] + [[i+k+0.1, -1] for i in nums]
        
        # ascending order, sort by first element then second element
        points.sort()

        # sweep over intervals
        beauty_current = beauty_max = 0
        for _, change in points:
            beauty_current += change
            beauty_max = max(beauty_max, beauty_current)

        return beauty_max
