class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        mp={}
        for i,v in reservedSeats: 
            if i in mp: 
                mp[i].append(v)
            else: 
                mp[i]=[v]

        print(mp)
        av=0
        for i in mp.keys():
            pre=1
            mid=1
            post=1
            for j in mp[i]:
                if j<=5 and j>1:
                    pre=0
                if j>=4 and j<=7:
                    mid=0
                if j>=6 and j<10:
                    post=0
            if pre==1 and post==1: 
                av+=2
            elif mid==1 or pre==1 or post==1: 
                av+=1
        av+=(n-len(mp.keys()))*2
        return av