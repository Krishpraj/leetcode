class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mapp={}
        for i in s:
            if i in mapp: 
                mapp[i]+=1
            else:
                mapp[i]=1

        print(mapp)
        for i in range(len(t)):
            if t[i] not in mapp or mapp[t[i]]==0: 
                return t[i]
            else: 
                mapp[t[i]]-=1


            