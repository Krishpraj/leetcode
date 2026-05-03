class Solution:
    def isValid(self, s: str) -> bool:
        
        mp={"}":"{","]":"[",")":"(" }
        st=[]
        s=[i for i in s ] 

        for i in range(len(s)):
            if s[i] not in mp:
                st.append(s[i]) 
            else:
                if not st or st[-1] is not mp[s[i]]:
                    return False 
                else:
                    st.pop()
    
        if st:
            return False 
        else:
            return True  