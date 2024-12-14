# Topics: Sliding Window

from collections import defaultdict

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0
        right = 0
        
        n = len(nums)
        C = defaultdict(int)
        C[nums[0]] += 1
        counter = 1  # nums[0:1] is continuous
        while right < n - 1:
            right += 1
            C[nums[right]] += 1

            v = nums[right]
            minv = v - 2
            maxv = v + 2

            # increase left until all nums[left:right] between v-2, v+2
            while True:
                keys = C.keys()
                if len(keys) == 0:
                    break
                if min(keys) < minv or max(keys) > maxv:
                    C[nums[left]] -= 1
                    if C[nums[left]] == 0:
                        del C[nums[left]]
                    left += 1
                else:
                    break
            counter += (right - left + 1)   # add subarray [left:left+1], [left:left+2], ... [left:right+1]
        return counter

