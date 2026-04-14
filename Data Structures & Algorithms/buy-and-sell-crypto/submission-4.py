class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        l = 0
        r = 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > m:
                m = profit
            if prices[r] < prices[l]:
                l = r
            r +=1
        return m
            
        