class Node:
    def __init__(self,key,val):
        self.prev=None 
        self.next=None 
        self.key=key
        self.val=val 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.lru=Node(0,0)
        self.mru=Node(0,0)
        self.lru.next=self.mru
        self.mru.prev=self.lru
    

    def remove(self,node): 
        left=node.prev
        right=node.next
        left.next=right
        right.prev=left

    def insert(self,node): 
        prev=self.mru.prev
        prev.next=node
        node.prev=prev
        node.next=self.mru 
        self.mru.prev=node

    def get(self, key: int) -> int:
        if key in self.cache: 
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val 
        else: 
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            node.val=value
        else: 
            if len(self.cache.keys())==self.capacity:
                self.cache.pop(self.lru.next.key)
                self.remove(self.lru.next) 
            node=Node(key,value)
            self.cache[key]=node
            self.insert(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)