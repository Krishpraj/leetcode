class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.prev=[]
    def get(self, key: int) -> int:
        if key in self.cache:
            self.prev.remove(key)
            self.prev.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.prev.remove(key)
            self.prev.append(key)
            self.cache[key]=value
        elif len(self.cache)<self.capacity:
            self.prev.append(key)
            self.cache[key]=value
        else:
            popped=self.prev.pop(0)
            pop=self.cache.pop(popped)
            self.cache[key]=value
            self.prev.append(key)



            
            



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)