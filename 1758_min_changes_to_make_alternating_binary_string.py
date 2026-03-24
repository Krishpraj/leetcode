class Solution:
    def minOperations(self, s: str) -> int:
        s=[int(c) for c in s]
        arrzero=[int(c) for c in s]
        arrone=[int(c) for c in s]
        szero=0
        sone=0

        for i in range(len(s)):
            if i==0:
                if s[i]==0:
                    sone+=1   
                else:
                    szero+=1
                arrzero[0]=0
                arrone[0]=1
            else:
                if arrzero[i]==arrzero[i-1]:
                    szero+=1
                    if arrzero[i]==1:
                        arrzero[i]=0
                    else:
                        arrzero[i]=1
                if arrone[i]==arrone[i-1]:
                    sone+=1
                    if arrone[i]==1:
                        arrone[i]=0
                    else:
                        arrone[i]=1
            
            print(szero,sone)
         
        return min(szero,sone)

    class Solution:
    def minOperations(self, s: str) -> int:
        even=[]
        odd=[]
        for i in range(len(s)):
            if i%2!=0:
                odd.append(s[i])
            else:
                even.append(s[i])         
        return min(odd.count("0")+even.count("1"), odd.count("1")+even.count("0"))

