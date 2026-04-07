class Robot:
    rotate = {
        (1,0):(0,1), 
        (0,1):(-1,0), 
        (-1,0):(0,-1), 
        (0,-1):(1,0)
    }
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = [0, 0]
        self.directions = (1, 0)
        self.perimeter = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        if self.perimeter == 0:
            return
        
        num %= self.perimeter
        if num == 0 and self.perimeter > 0:
            num = self.perimeter  # 🔥 FIX
        
        while num > 0:
            nx = self.pos[0] + self.directions[0]
            ny = self.pos[1] + self.directions[1]

            if 0 <= nx < self.width and 0 <= ny < self.height:
                self.pos = [nx, ny]
                num -= 1
            else:
                self.directions = self.rotate[self.directions]

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return {
            (0,1): "North",
            (-1,0): "West",
            (0,-1): "South",
            (1,0): "East"
        }[self.directions]
