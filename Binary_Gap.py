class Solution:
    def binaryGap(self, n: int) -> int:
        n=list(bin(n))[2:]
        n=[int(i) for i in n]

        mp=[]
        for i,v in enumerate(n):
            if v==1:
                mp.append(i)

        mxdistance=0      
        
        for i in range(len(mp)-1):
            mxdistance=max(mxdistance,mp[i+1]-mp[i])
    
        return mxdistance

