import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        profit = 0

        l = 0
        r = 1

        while r < len(prices):

            min_price = min(min_price, prices[l])
            profit = max(profit, prices[r] - prices[l])
            
            if min_price > prices[r]:
                l = r            

            r += 1

        return profit


        