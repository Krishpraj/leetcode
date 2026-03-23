class Solution:
    def longestBalanced(self, s: str) -> int:
        mxlen=0
        for i in range(len(s)):
            count={}
            for j in range(i,len(s)):
                if s[j] in count:
                    count[s[j]]+=1
                else:
                    count[s[j]]=1
                frequencies=list(count.values())
                if len(set(frequencies))==1:
                    mxlen=max(j-i+1,mxlen)
        
        return mxlen

