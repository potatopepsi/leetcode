# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    # Edge Case 1 - Both lists are empty, return one of them
    if((list1 == None) and (list2 == None)):
        return list1
    # Edge Case 2/3 - If one list is empty, return the other
    elif((list1 == None) and (list2 != None)):
        return list2
    elif((list1 != None) and (list2 == None)):
        return list1

    # Initializing output node and traversal node
    output = ListNode()
    trav = output

    # while loop - iterates through both lists and merges them
    while(True):
        try:
            if(list1.val < list2.val):
                tempNode = ListNode(list1.val)
                trav.next = tempNode
                trav = trav.next
                list1 = list1.next
            else:
                tempNode = ListNode(list2.val)
                trav.next = tempNode
                trav = trav.next
                list2 = list2.next
        except:
            break
    if(list1 != None):
        trav.next = list1
    elif(list2 != None):
        trav.next = list2

    
    output = output.next
    return output

