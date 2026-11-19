class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        total=nums
        prefix=[0]*len(nums)
        for i in range(0,len(nums)):
            if i>0:
                prefix[i]+=prefix[i-1]
            prefix[i]+=nums[i]
        
        
        count=0
        seen={0:1}
        for r in range(len(nums)):
            target=prefix[r]-k 
            if target in seen:
                count+=seen[target]
                
            if prefix[r] not in seen: 
                seen[prefix[r]]=0
            seen[prefix[r]]+=1
            
            


        return count 
        #   [-1,-2,-1]