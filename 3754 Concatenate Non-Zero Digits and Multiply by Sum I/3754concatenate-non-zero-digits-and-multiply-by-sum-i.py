class Solution:
    def sumAndMultiply(self, n: int) -> int:
        

        n=str(n)

        sum=0
        string=""
        for i in range(len(n)):
            if n[i]=="0":
                continue 
            sum+=int(n[i])
            string+=n[i]

        if n=="0":
            return 0 
        return int(string)*sum
