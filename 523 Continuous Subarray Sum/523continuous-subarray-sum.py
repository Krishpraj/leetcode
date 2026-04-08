class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        

        prefixsum=[0,nums[0]]
        prefixmod=[0,nums[0]%k]
        for i in range(1,len(nums)):
            prefixsum.append(prefixsum[-1]+nums[i])
            prefixmod.append(prefixsum[-1]%k)
        
        print(prefixmod)
        mp={}
        ans=0
        for i in range(len(prefixmod)):
            if prefixmod[i] not in mp:
                mp[prefixmod[i]]=i
            else:
                ans=max(ans,i-mp[prefixmod[i]])
        if ans>=2:
            return True
        else:
            return False
