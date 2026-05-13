class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        # use difference arrays 
        sums=[0]*(2*limit+2) 

        # ex. limit=4
        # [0,1,2,3,4,5,6,7,8]
        
        # we can do values from 2 to 8 


        for i in range(len(nums)//2):
            curr=nums[i]
            cp=nums[len(nums)-1-i]

            low=min(curr,cp)+1
            high=max(curr,cp)+limit

            sums[0]+=2
            sums[low]-=1
            sums[curr+cp]-=1
            sums[curr+cp+1]+=1
            sums[high+1]+=1
        
        arr=[0]*(2*limit+2) 
        curr=0
        for i in range(len(sums)):
            curr+=sums[i]
            arr[i]=curr
        
        return min(arr[2:len(sums)])
            


       




         