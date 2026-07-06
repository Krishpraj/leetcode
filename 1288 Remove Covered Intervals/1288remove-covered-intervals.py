class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key=lambda item: (item[0], -item[1]))
        rem=set()

        for i in range(len(intervals)):
            if tuple(intervals[i]) in rem: 
                continue 
            for j in range(i+1,len(intervals)):
                if intervals[i][0]<=intervals[j][0] and intervals[i][1]>=intervals[j][1]:
                    rem.add(tuple(intervals[j]))
                
        return len(intervals)-len(rem)

        