class LRUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.dList = DoublyLinkedList()
        self.capacity = capacity
        self.curr = 0

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        node = self.data[key]
        self.dList.remove(node)
        self.dList.insertBack(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.dList.remove(self.data[key])
            self.curr -= 1
        
        self.data[key] = self.dList.insertBack(Node(key, value))
        self.curr += 1
        if self.curr > self.capacity:
            lru = self.dList.popFront()
            del self.data[lru.key]
            self.curr -= 1
        
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insertBack(self, node):
        prev = self.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

        return node

    def popFront(self):
        prev = self.head.next
        nxt = prev.next
        self.head.next = nxt
        nxt.prev = self.head

        return prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

        return node

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None