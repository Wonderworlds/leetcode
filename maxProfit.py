class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0  # Buy
        right = 1  # Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]  # our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit


solution = Solution()
solution.maxProfit([7, 1, 5, 3, 6, 4])
solution.maxProfit([7, 6, 4, 3, 1])
