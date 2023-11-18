#Best Time to Buy and Sell Stock
#You are given an array prices where prices[i] is the price of a given stock on the ith day.You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
        # if not prices:
        #     print("0")
        # l=[]
        # for i in range(0,len(prices)):
        #     for j in range(i+1,len(prices)):
        #         k=prices[j]-prices[i]
        #         if k>0:
        #             l.append(k)
        # return max(l, default=0)
