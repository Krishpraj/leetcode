class Solution:
    def largestGoodInteger(self, num: str) -> str:

        l=0
        mx=-1
        for r in range(3,len(num)+1):
            
            se=set(num[l:r])
            
            if len(se)==1:
                print(se)
                mx=max(mx,int(se.pop()))
            l+=1

        if mx==-1:
            return ""
        else:
            return f"{mx}{mx}{mx}"