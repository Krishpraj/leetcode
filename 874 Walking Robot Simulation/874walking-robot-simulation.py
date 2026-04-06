class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obstacles=set(tuple(i) for i in obstacles)
        drx=0 #going up
        dry=1  # going up

        # location
        tx=0
        ty=0
        
        maxdist=0
        right={(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1)}
        left={(0,1):(-1,0),(-1,0):(0,-1),(0,-1):(1,0),(1,0):(0,1)}

        for i in commands:
            if i==-2:
                drx,dry=left[(drx,dry)]
            
            elif i==-1:
                drx,dry=right[(drx,dry)]

            else:
                temp=i
                while temp!=0:
                    tx+=drx
                    ty+=dry

                    if (tx,ty) in obstacles:
                        tx=tx-drx
                        ty=ty-dry
                        temp=1

                    temp-=1

                maxdist=max(maxdist,tx**2+ty**2)

        return maxdist
