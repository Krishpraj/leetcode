class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total=sum(sum(i) for i in grid)
    
        def partition(arr):
            sm=0
            seen=set()
            for i in range(len(arr)-1):
                sm+=sum(arr[i])
                seen |= set(arr[i])


                if sm==total-sm:
                    return True 
                if sm-arr[0][len(arr[0])-1]==total-sm:
                    return True 
                if sm-arr[0][0]==total-sm:
                    return True 
                if sm-arr[i][0]==total-sm:
                    return True
                
                if i>0 and len(arr[0])>1 and (2*sm-total) in seen:
                    return True 

            return False 

        
        return (partition(grid) or partition(grid[::-1]) or partition(list(zip(*grid))) or partition(list(zip(*grid))[::-1]))
                
