# Topics: Array, Two pointers, Greedy
# Time complexity O(n)
# See the good explination about the greedy algorithm here
# https://leetcode.com/problems/container-with-most-water/solutions/6099/yet-another-way-to-see-what-happens-in-the-o-n-algorithm

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        best = 0
        while left < right:
            best = max(best, min(height[left], height[right]) * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best

