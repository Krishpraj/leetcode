class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        s1=[c for c in s1]
        s2=[c for c in s2]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                # compare s1 with s2
                for j in range(i+1,len(s1)):
                    if s1[j]==s2[i] and j-i==2:
                        s1[i],s1[j]=s1[j],s1[i]
            else:
                continue 
        print(s1,s2)
        return s1==s2