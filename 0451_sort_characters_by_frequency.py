class Solution:
    def frequencySort(self, s: str) -> str:
        s=[c for c in s]
        mapp={}
        for i in s: 
            if i in mapp: 
                mapp[i]+=1
            else:
                mapp[i]=1        

        mapp= dict(sorted(mapp.items(), key=lambda item: item[1],reverse=True))
        string=""
        for i in mapp.keys(): 
            while mapp[i]!=0:
                string=string+i
                mapp[i]-=1
        return string