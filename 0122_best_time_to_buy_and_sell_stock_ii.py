class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dfs(idx, status):
            if idx == len(prices):
                return 0

            if (idx, status) in memo:
                return memo[(idx, status)]

            if status == 0:  # can sell
                res = max(
                    dfs(idx + 1, 0),           
                    dfs(idx + 1, 1) + prices[idx]
                )
            else:  # can buy
                res = max(
                    dfs(idx + 1, 1),            
                    dfs(idx + 1, 0) - prices[idx] 
                )

            memo[(idx, status)] = res
            return res

        return dfs(0, 1)
