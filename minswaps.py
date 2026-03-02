class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        mp=[]
        for i in range(len(grid)):
            r=len(grid[i])-1
            count=0
            while grid[i][r]==0 and r>=0:
                count+=1
                r-=1
            mp.append(count)

        # index and count of zeroes 
        swaps=0
        for i in range(len(grid)):
            needed=len(grid)-i-1
            print(mp)
            idx=None 
            for j in range(i,len(mp)):
                if mp[j]>=needed:
                    idx=j
                    break

            if idx is None :
                return -1
            
            print(idx)
            for j in range(idx,i,-1):
                temp=mp[j-1]
                mp[j-1]=mp[j]
                mp[j]=temp
                swaps+=1

        return swaps    
            


