class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        ct=0
        for i in s:
            if i=="(":
                st.append("(")
            else:
                if st:
                    st.pop()
                else:
                    ct+=1
        return ct+len(st)

        return max(o,c)-min(o,c)
    #    def dfs(i,opened,closed):
    #     if s[i]=="(":
    #         opened+=1
    #     else:
    #         closed+=1

    #     rs1=dfs(i+1,opened,closed+1)+1
    #     rs2=dfs(i+1,opened+1,closed)+1
    #     rs3=dfs(i+1,opened,closed)

