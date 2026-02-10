class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        max_size=0

        
        for l in range(len(nums)):
            even_count=0
            odd_count=0 
            seen=set()
            for r in range(l,len(nums)):
                if nums[r]%2==1 and nums[r] not in seen:
                    odd_count+=1
                    seen.add(nums[r])
                elif nums[r]%2==0 and nums[r] not in seen:
                    even_count+=1
                    seen.add(nums[r])
                else:
                    pass 

                if odd_count==even_count and r-l+1>max_size:
                    max_size=r-l+1
            

        return max_size 