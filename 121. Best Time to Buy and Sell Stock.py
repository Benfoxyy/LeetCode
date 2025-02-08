prices = prices = [7,6,4,3,1]

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for i in prices[1:]:
            if i < buy_price:
                buy_price = i
            else:
                profit = max(profit, i - buy_price)
        return profit
        
print(Solution().maxProfit(prices))