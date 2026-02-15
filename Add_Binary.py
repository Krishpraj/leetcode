class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a=[int(c) for c in a]
        b=[int(c) for c in b] 
        carry=0
        ans=[]
        while a or b:
            temp1,temp2=0,0
            if a:
                temp1=a.pop()
            if b:
                temp2=b.pop()
            print(temp1,temp2)
            
            sm=(temp1+temp2+carry)%2
            carry=(temp1+temp2+carry)//2
                

            ans.insert(0,sm)
            print("answer",ans)
            print("carry", carry)
        
        if carry>0:
            ans.insert(0,carry)

        ans=[str(c) for c in ans]
        return "".join(ans)
            