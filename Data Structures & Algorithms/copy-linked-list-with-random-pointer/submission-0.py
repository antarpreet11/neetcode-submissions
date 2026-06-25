"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {None: None}
        tmp = head

        while tmp is not None:
            nodeMap[tmp] = Node(tmp.val)
            tmp = tmp.next
        
        tmp = head

        while tmp:
            nodeMap[tmp].next = nodeMap[tmp.next]
            nodeMap[tmp].random = nodeMap[tmp.random]
            tmp = tmp.next
        
        return nodeMap[head]