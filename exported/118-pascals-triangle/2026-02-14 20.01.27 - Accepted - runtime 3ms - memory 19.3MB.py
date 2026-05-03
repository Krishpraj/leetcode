class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res=[[1]]
        for i in range(1,numRows):
            temp=res[-1]
            ans=[0]*(len(temp)+1)
            for j in range(len(temp)):
                ans[j]+=temp[j]
                ans[j+1]+=temp[j]
            res.append(ans)

        return res
            