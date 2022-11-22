# Score:
#  Runtime: 51%
#  Memory usage: 37%
#
# Description:
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# Find the maximum profit you can achieve. You may complete at most two transactions.
#

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_options = []
        sell_options = []
        buy = prices[0]
        buy_at = 0
        sell = None
        sell_at = None
        
        # Find all buy and sell best points
        for i, price in enumerate(prices[1:], start=1):
            if sell is None and price > buy or sell is not None and price > sell:
                sell = price
                sell_at = i
            elif sell and price < sell:
                sell_options.append((sell, sell_at))
                buy_options.append((buy, buy_at))
                buy = price
                buy_at = i
                sell = None
            elif price < buy:
                buy = price
                buy_at = i
        
        if sell:
            buy_options.append((buy, buy_at))
            sell_options.append((sell, sell_at))
        
        sell_options = sorted(sell_options, key=itemgetter(0), reverse=True)
        buy_options = sorted(buy_options, key=itemgetter(0))
        
        best = 0
        best_from_2 = False
        
        # Search for the best non overlapping buy and sell options
        for i, (low, buy_at) in enumerate(buy_options):
            for high, sell_at in sell_options:
                if sell_at <= buy_at:
                    continue
                
                amount = high - low
                
                if best_from_2 and amount * 2 < best:
                    break
                
                if amount > best:
                    best = amount
                
                for low2, buy_at2 in buy_options[i+1:]:
                    for high2, sell_at2 in sell_options:
                        if sell_at2 <= buy_at2 or sell_at2 == sell_at:
                            continue
                            
                        amount2 = high2 - low2
                        
                        if amount + amount2 <= best:
                            break
                            
                        if sell_at2 < buy_at or buy_at2 > sell_at:
                            best = amount + amount2
                            best_from_2 = True
        return best
      
