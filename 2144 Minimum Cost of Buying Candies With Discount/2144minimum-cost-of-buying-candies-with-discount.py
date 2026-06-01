class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        

        cost.sort()
        costs=0
        for i in range(len(cost),-1,-3):
            if 0<=i<len(cost): 
                costs+=cost[i]
        
        return sum(cost)-costs
