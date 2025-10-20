class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        buy_day = 0
        sell_day = buy_day + 1
        while sell_day <= len(prices) - 1:
            if prices[sell_day] - prices[buy_day] < 0:
                buy_day = sell_day 
            elif prices[sell_day] - prices[buy_day] > best_profit:
                best_profit = prices[sell_day] - prices[buy_day]
            sell_day += 1
        return best_profit