class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[]
        ans=0
        for i in range(len(nums)): # 0, 1 , 2
            ans=ans<<1 # 00
            ans=ans|nums[i] 
            if ans%5==0:
                res.append(True)
            else:
                res.append(False)
        return res 
