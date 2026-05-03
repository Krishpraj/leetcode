class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        directions={"L":(1,0),"U":(0,1),"R":(-1,0),"D":(0,-1)}

        tx=0
        ty=0

        for i in range(len(moves)):
            drx, dry = directions[moves[i]]
            tx+=drx
            ty+=dry
        
        if tx==0 and ty==0:
            return True 
        else:
            return False
