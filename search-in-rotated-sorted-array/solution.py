# Topics: binary search

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)
            if nums[mid] == target:
                return mid
            elif left == mid:   # nothing in left part, search right part
                left = mid + 1
            elif left == mid - 1 and nums[left] == target:
                return left
            elif nums[left] < nums[mid-1] and nums[left] <= target and nums[mid-1] >= target:
                right = mid - 1
            elif nums[left] > nums[mid-1] and (nums[left] <= target or  nums[mid-1] >= target):
                right = mid - 1
            else:
                left = mid + 1
        return -1
