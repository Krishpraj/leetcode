class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        se={}
        for i in nums:
            if i not in se:
                se[i]=1
            else:
                se[i]+=1
        d=-1
        r=-1
        for i in range(1,len(nums)+1):
            if i not in se:
                r=i
            elif se[i]==2:
                d=i
        return [d,r]