class Solution:
    def minInsertions(self, s: str) -> int:
        
        idx=0
        st=[]
        count=0
        while idx<len(s):
            if s[idx]=="(":
                st.append("(")
                idx+=1
            else:
                if not st:
                    if idx+1<len(s) and s[idx+1]==")":
                        count+=1
                        idx+=2
                    else:
                        count+=2
                        idx+=1
                elif idx+1<len(s) and s[idx+1]==")":
                    st.pop()
                    idx+=2
                else:
                    count+=1
                    st.pop()
                    idx+=1
                    
        count+=len(st)*2
        return count 
