class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        

        res=[[poured]]
        for i in range(1,query_row+1):
            temp=res[-1]
            ans=[0]*(len(temp)+1)
            for j in range(len(temp)):
                if (temp[j]-1)/2>=0:
                    ans[j]+=(temp[j]-1)/2
                    ans[j+1]+=(temp[j]-1)/2
            res.append(ans)
        print(res)
        ans=res[query_row][query_glass]
        if ans>=1:
            return 1
        elif ans<=0:
            return 0
        else:
            return ans

        