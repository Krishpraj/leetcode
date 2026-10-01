class Solution:
    def isValid(self, s: str) -> bool:


        st=[]
        brackets={")":"(","]":"[","}":"{"}
        for i in range(len(s)):
            if s[i] in brackets:
                if st and st[-1]==brackets[s[i]]:
                    st.pop()
                else:
                    return False 
            else:
                st.append(s[i])
        
        return len(st)==0
        