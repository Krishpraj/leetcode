class Solution:
    def countTriples(self, n: int) -> int:
        triples=0
        se=set()
        for i in range(1,n+1):
            print(se)
            for j in se:
                if i**2-j in se:
                    print(i**2,j)
                    triples+=1 
            se.add(i**2)
        
        return triples
            