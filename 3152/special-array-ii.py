def parity(x):
    return x % 2

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        A = [0] * n
        for i in range(1, n):
            if parity(nums[i]) != parity(nums[i-1]):
                A[i] = A[i-1]   # extend speical subarray
            else:
                A[i] = A[i-1] + 1   # start a new speical subarray
        
        ans = []
        for (f, t) in queries:
            ans.append(A[f] == A[t])

        return ans
