class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        mp={}
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]]+=1
            else:
                mp[nums[i]]=1
        
        heap=[]

        for i,v in mp.items():
            heapq.heappush(heap,(-v,i))
        
        res=[]
        for i in range(k):
            freq,num=heapq.heappop(heap)
            res.append(num)

        return res 