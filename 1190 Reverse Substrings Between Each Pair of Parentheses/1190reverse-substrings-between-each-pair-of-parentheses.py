class Solution:
    def reverseParentheses(self, s: str) -> str:

        st=[[]]
        for i in range(len(s)):
            if s[i]=="(":
                st.append([])
            elif s[i]==")":
                prev=st.pop()
                st[-1].extend(prev[::-1])
            else:
                st[-1].append(s[i])
        return str("".join(st[0]))
        
        