class Solution:
    def rob(self, nums: List[int]) -> int:
        mp={}
        def money(i):
            if i==0:
                mp[i]=nums[0]
                return
            elif i==1:
                mp[i]=max(nums[0],nums[1])
                return 
            mp[i]=max(mp[i-2]+nums[i],mp[i-1])

        for i in range(len(nums)):
            money(i)

        print(mp)
        return mp[len(nums)-1]