class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret=[int(c) for c in secret]
        guess= [int(c) for c in guess]
        mp={}
        ctb=0
        ctc=0

        for i,v in enumerate(secret):
            if secret[i]==guess[i]:
                ctb+=1
                guess[i]=-1
            else:
                if v not in mp:
                    mp[v]=[i]
                else:
                    mp[v].append(i)
        print(mp)
        for i in guess:
            if i in mp:
                ctc+=1
                if i in mp and len(mp[i])==1:
                    mp.pop(i)
                else:
                    mp[i].pop()
        
        return str(ctb)+"A"+str(ctc)+"B"
        
        print(ctb,ctc)
        