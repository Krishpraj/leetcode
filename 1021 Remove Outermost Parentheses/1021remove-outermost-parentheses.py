class Solution:
    def removeOuterParentheses(self, s: str) -> str:

       res=[]
       st=[]     
       for i in range(len(s)):
        if s[i]=='(':
            st.append("(")
        
        if len(st)>1:
            res.append(s[i])

        if s[i]==")":
            st.pop()
        
        print(st)
        
        
       return "".join(res)