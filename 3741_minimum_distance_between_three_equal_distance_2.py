class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        mp={}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]]=[i]
            else:
                mp[nums[i]].append(i)
        
        mindistance=float('inf')
        for i in mp.values():
            if len(i)>=3:
                for j in range(len(i)-2):
                    temp=abs(i[j] - i[j+1]) + abs(i[j+1] - i[j+2]) + abs(i[j+2] - i[j])
                    if temp<mindistance:
                        mindistance=temp
        

        if mindistance==float('inf'):
            return -1
        else:
            return mindistance
            
