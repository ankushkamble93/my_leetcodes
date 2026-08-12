class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.storage:
            return -1
        self.storage.move_to_end(key)
        return self.storage[key]

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.storage.move_to_end(key)
        self.storage[key] = value
        if len(self.storage) > self.capacity:
            self.storage.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)