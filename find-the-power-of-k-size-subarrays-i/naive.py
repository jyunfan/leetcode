# Time complexity: O(nk)
# Space complexity: O(n+k)

class Solution:
    def power(self, nums):
        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                return -1

        return nums[-1]

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        output = [0] * (n - k + 1)
        for i in range(n - k + 1):
            output[i] = self.power(nums[i:i+k])
        return output
