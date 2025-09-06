class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.maxCapacity = capacity
        self.currentCapacity = 0
        self.order = []
        

    def get(self, key: int) -> int:
        if(self.cache.get(key)==None):
            return -1
        else:
            self.order.remove(key)
            self.order.append(key)
            return self.cache.get(key)
        

    def put(self, key: int, value: int) -> None:
        if(self.get(key) == -1):
            if(self.currentCapacity == self.maxCapacity):
                temp = self.order[0]
                self.cache.pop(temp)
                self.order.remove(temp)
                self.currentCapacity -= 1
        
            self.cache.update({key: value})
            self.currentCapacity += 1
            self.order.append(key)
        else:
            self.cache.update({key: value})
            self.order.remove(key)
            self.order.append(key)
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)