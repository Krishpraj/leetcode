class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        
        res=[]
        counter=0
        for i,v in enumerate(seq):
            if counter%2==0 and v=="(":
                res.append(1)
                counter+=1
            elif counter%2==1 and v=="(":
                res.append(0)
                counter+=1

            if v==")":
                counter-=1
                if counter%2==0:
                    res.append(1)
                else:
                    res.append(0)
                
                
            
        
        return res 

            
