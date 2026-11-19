class Solution:
    def countAndSay(self, n: int) -> str:

        def convert(n):
            x=n
            res=""
            counter=0
            value=x[0]
            for i in range(len(x)):
                if x[i]==value:
                    counter+=1
                else: 
                    res+=f"{counter}{value}"
                    counter=1
                    value=x[i]
            res+=f"{counter}{value}"
            return res

        count="1"
        if n==1: 
            return count
        else: 
            for i in range(2,n+1):
                count=convert(count)
        return count