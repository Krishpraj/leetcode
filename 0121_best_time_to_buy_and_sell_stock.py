class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r=0

        profit=0
        minprice=float('inf')

        while r<len(prices):
            if prices[r]<minprice:
                minprice=prices[r]
            else:
                profit=max(profit,prices[r]-minprice)

            r+=1

        return profit 
         

