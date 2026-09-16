class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key= lambda item:item[0])
        
        res=[intervals[0]]
        ptr=1
        while ptr<len(intervals):
            curr=intervals[ptr]
            if curr[0]<=res[-1][1]:
                prev=res.pop()
                new=[prev[0],max(prev[1],curr[1])]
                res.append(new)
            else:
                res.append(curr)
            ptr+=1
        
        return res 