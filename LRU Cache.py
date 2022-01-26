class Node(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.left = Node(float("-inf"),0)
        self.right = Node(float("inf"),0)
        self.left.next = self.right
        self.right.prev = self.left
            
    def insert(self,node):
        pre = self.right.prev
        nxt = self.right
        pre.next = node
        node.prev = pre
        node.next = nxt
        nxt.prev = node
    def remove(self,node):
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
        
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
k = obj.get(1)
print(k)
obj.put(3,3)
k1 = obj.get(2)
print(k1)
obj.put(4,4)
k2 = obj.get(1)
print(k2)
k3 = obj.get(3)
print(k3)
k4 = obj.get(4)
print(k4)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

       

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
