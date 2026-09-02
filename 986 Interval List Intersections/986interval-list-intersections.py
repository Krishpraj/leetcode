class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        res=set()
        for i,j in firstList:
            for k,v in secondList:
                if i<=k<=j:
                    res.add((k,min(j,v)))
                if k<=i<=v:
                    res.add((i,min(j,v)))

        res=sorted(res, key= lambda item:item[0])
        return res     