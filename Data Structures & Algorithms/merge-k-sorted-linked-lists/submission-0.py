# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def merge2Lists(list1: Optional[ListNode], list2: Optional[ListNode]) ->              Optional[ListNode]:
            new = curr = ListNode()

            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            curr.next = list1 or list2

            return new.next

        def binaryMerge(lists: List[Optional[ListNode]]) -> List[Optional[ListNode]]:
            tempLists = []
            length = len(lists)
            i = 0

            while i < length:
                if i + 1 < length:
                    tempLists.append(merge2Lists(lists[i], lists[i + 1]))
                else:
                    tempLists.append(lists[i])
                i += 2
            return tempLists
        
        while len(lists) > 1:
            lists = binaryMerge(lists)
        
        return lists[0]
                           
