from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        left, right = 0, len(nums)-1
        while left < right:
            mid = int((left+right)/2)
            # Update possible minimum we have seen so far
            minimum = min([minimum, nums[mid], nums[left], nums[right]])
            # check left
            if mid-1 <= left or nums[left] < nums[mid-1]: # left part is ascending
                # continue to search possible minimun in the right part
                left = mid + 1
            else:
                # continue to search possible minimun in the left part
                right = mid - 1
        return minimum
