class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        delta = 0
        start = None
        if prices is None or len(prices) < 2:
            return 0
        for x in range(0, len(prices) - 1):
            if (start is not None) and (x < start):
                continue
            for y in range(x + 1, len(prices)):
                if prices[y] - prices[x] > delta:
                    delta = prices[y] - prices[x]
                    start = x
        print(delta)


solution = Solution()
solution.maxProfit([7, 1, 5, 3, 6, 4])
solution.maxProfit([7, 6, 4, 3, 1])
