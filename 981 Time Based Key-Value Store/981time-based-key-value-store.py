class TimeMap:

    def __init__(self):
        self.vl={}
        self.tm={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.vl:
            self.tm[key]=[] 
            self.vl[key]=[]   
        self.vl[key].append(value)
        self.tm[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""

        curr=self.tm[key]
        if curr[0] > timestamp:
            return ""


        l=0
        r=len(curr)-1
        
        while l<r:
            mid=(r+l+1)//2
            if curr[mid]<=timestamp:
                l=mid
            else:
                r=mid-1
        
        
        return self.vl[key][l]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)