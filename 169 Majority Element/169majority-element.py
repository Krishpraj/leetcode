class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        mp={}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]]=1
            else:
                mp[nums[i]]+=1
            
            if mp[nums[i]]>len(nums)//2:
                return nums[i]
        


        