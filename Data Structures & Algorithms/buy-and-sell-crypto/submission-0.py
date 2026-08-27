class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_p = 0
        while r < len(prices):
            # 1. Check if the sell price is > buy price - thus profit
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                # 2. There is a loss - move to better buying price
                l = r
            r += 1
        
        return max_p
