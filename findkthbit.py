class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def series(n):
            if n==1:
                return "0"
            else:
                temp=series(n-1)
                temp2=[]
                for i in range(len(temp)):
                    if temp[i]=="0":
                        temp2.append("1")
                    else:
                        temp2.append("0")
                temp2.reverse()
                rev_temp="".join(temp2)
                return temp+"1"+rev_temp
        
        
        ans=series(n)
        print(ans)
        return ans[k-1]

        
        

