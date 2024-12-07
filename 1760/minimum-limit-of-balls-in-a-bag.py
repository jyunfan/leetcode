# Interesting question!
# Topics: binary search
# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

# calculate how many operations we need to make all nums <= max_n after split
def cal(nums, max_n):
    s = 0
    for i in nums:
        if i <= max_n:
            continue
        if i % max_n == 0:
            s += i // max_n - 1
        else:
            s += i // max_n
    return s

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()
        left, right = 1, nums[-1]
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            operations_need = cal(nums, mid)

            if operations_need > maxOperations:
                left = mid + 1
            else:
                ans = mid   # update best ans
                right = mid - 1

        return ans
    
