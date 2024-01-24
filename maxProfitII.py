class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return sum(
            (prices[idx + 1] - prices[idx])
            for idx in range(len(prices) - 1)
            if prices[idx] < prices[idx + 1]
        )


solution = Solution()
solution.maxProfit([7, 1, 5, 3, 6, 4])
solution.maxProfit([7, 6, 4, 3, 1])
