class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:


       idx=0
       res=[]
       placed=False
       while idx<len(intervals):
        if not placed:
            if newInterval[0]>=intervals[idx][0] and newInterval[0]<=intervals[idx][1]:
                res.append([min(intervals[idx][0],newInterval[0]),max(intervals[idx][1],newInterval[1])])
                placed=True
            elif newInterval[0]<intervals[idx][0]:
                res.append(newInterval)
                placed=True 
            
        if res and intervals[idx][0]<=res[-1][1]:
            res[-1][1]=max(intervals[idx][1],res[-1][1])
        else:
            res.append(intervals[idx])
        idx+=1
       
       if not placed:
        res.append(newInterval)
       return res 
        
