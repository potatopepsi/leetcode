# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Helper Function
# noneClear - removes any None types in the list
def noneClear(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    try:
        for i in range(lists.count(None)):
            lists.remove(None)
    except:
        pass
    return lists

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

    # Initializing output node
    output = ListNode()
    lists = noneClear(lists)

    # Edge Case - Empty List
    if(len(lists)==0):
        output = output.next
        return output
    
    trav = output

    # Average Case
    while(len(lists) != 0):
        # Initializing temporary variables
        minIterator = 0
        minValue = 10**4

        
        for i in range(len(lists)):
            if(lists[i].val <= minValue):
                minIterator = i
                minValue = lists[i].val
        newNode = ListNode(minValue)
        trav.next = newNode
        trav = trav.next
        lists[minIterator] = lists[minIterator].next
        lists = noneClear(lists)
    
    output = output.next
    return output



        
