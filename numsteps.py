cclass Solution:
    def numSteps(self, s: str) -> int:
        count=0
        while int(s,2)!=1:
            if int(s,2)%2==1:
                s=int(s,2)+1
                s=bin(s)
            else:
                s=int(s,2)//2
                s=bin(s)
            count+=1

        return count 


