class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        

        count=0
        mp={}
        mp[0]=[-1]
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count-=1

            if count in mp:
                mp[count].append(i)
            else:
                mp[count]=[i]
        
        mx=0
        for i in mp.values():
            if len(i)>=2:
                mx=max(mx,max(i)-min(i))
        return mx 
                
        
