class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = [0] * n
        for i in range(n):
            answer[i] = prices[i]
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    answer[i] = prices[i] - prices[j]
                    break
        return answer
