class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.capacity = capacity
        self.cache = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def addToTail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail.prev.next
        self.tail.prev.next = node
        self.tail.prev = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # recent visit
        node = self.cache[key]
        self.removeNode(node)
        self.addToTail(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.addToTail(node)
        else:
            if len(self.cache) == self.capacity:
                lruNode = self.head.next
                self.removeNode(lruNode)
                self.cache.pop(lruNode.key)
            node = ListNode(key, value)
            self.cache[key] = node
            self.addToTail(node)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)