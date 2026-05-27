import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        lowest_stock_price = math.inf

        l = 0
        r = 1

        if len(prices) <= 1:
            return 0

        while r < len(prices):
            cost_price = prices[l]
            selling_price = prices[r]

            profit = selling_price - cost_price

            if cost_price > selling_price:
                l = r
                r = l + 1
            else:
                r += 1

            max_profit = max(max_profit, profit)

        return max_profit


        