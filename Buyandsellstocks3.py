                                                                   
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dfs(idx, status, count):
            if idx == len(prices) or count==2:
                return 0


            if (idx, status, count) in memo:
                return memo[(idx, status, count)]

            if status == 0:  # can sell
                res = max(
                    dfs(idx + 1, 0, count),           
                    dfs(idx + 1, 1, count+1) + prices[idx]
                )
            else:  # can buy
                res = max(
                    dfs(idx + 1, 1, count),            
                    dfs(idx + 1, 0, count) - prices[idx] 
                )

            memo[(idx, status, count)] = res
            return res

        return dfs(0, 1,0)
